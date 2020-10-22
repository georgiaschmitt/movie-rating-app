"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    if row == None:
        print(f"Could not find {github}")
    else:
        print("Student: {} {}\nGitHub account: {}".format(
            row[0], row[1], row[2]))


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    QUERY = """
        INSERT INTO students (first_name, last_name, github)
          VALUES (:first_name, :last_name, :github)
        """

    db.session.execute(QUERY, {'first_name': first_name,
                               'last_name': last_name,
                               'github': github})
    db.session.commit()

    print(f"Successfully added student: {first_name} {last_name}")


def get_project_by_title(title):
    """Given a project title, print information about the project."""

    QUERY = """
        SELECT * 
        FROM projects
        WHERE title = :title
        """
    db_cursor = db.session.execute(QUERY, {'title': title})

    row = db_cursor.fetchone()

    if row == None:
        print(f"Could not find {title}")
    else:
        print(f"Title: {row[1]} \nDescription: {row[2]} \nMax_Grade: {row[3]}")


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    QUERY = """
        SELECT grade
        FROM grades
        WHERE student_github = :github_s AND project_title = :title_p
        """
    db_cursor = db.session.execute(
        QUERY, {'github_s': github, 'title_p': title})

    row = db_cursor.fetchone()

    if row == None:
        print(f"Could not find project {title} for {github}")
    else:
        print(f"Grade: {row[0]}")

def project_exist(title):

    QUERY = """
        SELECT * 
        FROM projects
        WHERE title = :title
        """
    db_cursor = db.session.execute(QUERY, {'title': title})

    row = db_cursor.fetchone()

    return row != None


def student_exist(github):

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    return row != None



def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""

    if not project_exist(title):
        print(f"Could not assign grade for {title}: no such project")
        return

    if not student_exist(github):
        print(f"Could not assign grade for {github}: no such github account")
        return


    QUERY = """
        INSERT INTO grades (student_github, project_title, grade)
        VALUES (:github, :title, :grade)
    """
    db.session.execute(
        QUERY, {'github': github, 'title': title, 'grade': grade})
    db.session.commit()

    print(
        f"Successfully assign {github} with the project {title} at grade {grade}")


def add_project(title, description, max_grade):

    QUERY = """
        INSERT INTO projects (title, description, max_grade)
        VALUES (:title, :description, :max_grade)
    """
    db.session.execute(
        QUERY, {'title': title, 'description': description, 'max_grade': max_grade})
    db.session.commit()

    print(f"Successfully added project {title}")


def get_all_grades(github):

    QUERY = """
        SELECT project_title, grade
        FROM grades
        WHERE student_github = :github   
        """
    db_cursor = db.session.execute(QUERY, {'github': github})
    rows = db_cursor.fetchall()

    if rows == None:
        print(f"Could not get grades for {github}")
    else:
        for row in rows:
            title, grade = row
            print(f"Student {github} has grade {grade} for {title}")


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            if len(args) != 1:
                print("Invalid input, please use: student [github]")
            else:
                github = args[0]
                get_student_by_github(github)

        elif command == "new_student":
            if len(args) != 3:
                print("Invalid input, please use: new_student [first_name] [last_name] [github]")
            else:
                first_name, last_name, github = args  
                make_new_student(first_name, last_name, github)

        elif command == "project":
            if len(args) != 1:
                print("Invalid input, please use: project [title]")
            else:
                title = args[0]
                get_project_by_title(title)

        elif command == "grade":
            if len(args) != 2:
                print("Invalid input, please use: grade [github] [title]")
            else:
                github, title = args
                get_grade_by_github_title(github, title)

        elif command == 'assign_grade':
            if len(args) != 3:
                print("Invalid input, please use: assign_grade [github] [title] [grade]")
            else:
                github, title, grade = args
                assign_grade(github, title, grade)

        elif command == 'add_project':
            if len(args) < 3:
                print("Invalid input, please use: add_project [title] [description] [max_grade]")
            else:
                title = args[0]
                description = ' '.join(args[1:-1])
                max_grade = int(args[-1])
                add_project(title, description, max_grade)

        elif command == 'grades':
            if len(args) != 1:
                print("Invalid input, please use: grades [github]")
            else:
                github = args[0]
                get_all_grades(github)

        else:
            if command != "quit":
                print("Invalid Entry. Try again.")


if __name__ == "__main__":
    connect_to_db(app)

    # handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    db.session.close()
