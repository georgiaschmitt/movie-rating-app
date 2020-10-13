"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      Hi! This is the home page.
      <a href="http://0.0.0.0:5000/hello">Start here</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <a>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div>What's your name?
            <input type="text" name="person">
          </div>
          <div>
            <label>Choose your compliment:</label>
          <select name="compliment">
              <option value="awesome">Awesome</option>
              <option value="terrific">Terrific</option>
              <option value="fantastic">Fantastic</option>
              <option value="neato">Neato</option>
          </select>
          </div>
          <input type="submit" value="Submit"> 
        </form>
        <form action="/diss">
          <div>What's your name?
            <input type="text" name="person">
          </div>
          <div ">
            <label>What diss do you want to hear?</label>
            <input type="radio" name="diss" value="ugly">
            <label>Ugly</label>
            <input type="radio" name="diss" value="mean">
            <label>Mean</label>
            <input type="radio" name="diss" value="lazy">
            <label>Lazy</label>
          </div>
          <input type="submit" value="Submit"> 
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
  <!doctype html>
  <html>
    <head>
      <title>A Diss</title>
    </head>
    <body>
      Hi, {}! I think you're {}!
    </body>
  </html>
  """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
