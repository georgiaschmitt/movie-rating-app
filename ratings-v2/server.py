"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    if 'user_id' in session:
        return render_template("homepage.html")
    else:
        return render_template("login.html")


@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.get_all_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def get_movie(movie_id):
    """ Show a movie's detail """

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/users")
def all_users():
    """View all users."""
    users = crud.get_all_users()
    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def get_user(user_id):
    """Return user by id."""
    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)


@app.route('/new-user', methods=['POST'])
def create_user():
    """ Create a new user """
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash("We already had an account associated with that email, please use a new email")
    else:
        crud.create_user(email, password)
        flash("Your account is created successfully. You can now log in")

    return redirect("/")

@app.route('/user-login')
def user_login():
    """Log a user in."""
    email = request.args.get("login_email")
    password = request.args.get("login_password")

    if crud.password_match(email, password):
        user = crud.get_user_by_email(email)
        session['user_id'] = user.user_id
        flash("Logged in")
    else:
        flash("Your email and password do not match")
    
    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
