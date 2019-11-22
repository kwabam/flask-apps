# Blog Flask application

import os
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g

# PostgreSQL IP address
IP_ADDR = "127.0.0.1"

# Create the application
app = Flask(__name__)


#####################################################
# Database handling

def connect_db():
    """Connects to the database."""
    debug("Connecting to DB.")

    conn = psycopg2.connect("dbname=newdle user=kevin password=pandas300")
    return conn


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'pg_db'):
        g.pg_db = connect_db()
    return g.pg_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database automatically when the application
    context ends."""
    debug("Disconnecting from DB.")
    if hasattr(g, 'pg_db'):
        g.pg_db.close()


######################################################
# Command line utilities

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().execute(f.read())
    db.commit()


@app.cli.command('initdb')
def init_db_command():
    """Initializes the database."""
    print("Initializing DB.")
    init_db()


#####################################################
# Debugging

def debug(s):
    """Prints a message to the screen (not web browser)
    if FLASK_DEBUG is set."""
    if app.config['DEBUG']:
        print(s)


@app.route('/')
def login():
    # form_data = request.form
    # if form_data['Username'] == "" or form_data['Password']== "":
    #     return render_template("login.html")
    #
    # print(form_data['Username'])
    # print(form_data['Password'])
    return render_template("login.html")


@app.route('/home')
def home():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
            select * from lectures where crn = 
        """)
    # days = []
    # year = "2019"
    # month = "9"
    # day = 1
    # for i in range(31):
    #     lecture_date = year + "-" + month + "-" + str(day)
    #     day += 1
    #     cursor.execute("""
    #                 select * from lectures where lecturedate = lecture_date
    #             """)
    #     days.append(cursor.fetchall())
    # calendar = cursor.fetchall()
    return render_template("homepage.html")


@app.route('/day')
def day():
    db=get_db()
    cursor=db.cursor()
    cursor.execute("""
        select * from lectures where lecturedate = '2019-03-14'
    """)
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("dayview.html", studentinfo=rowList)

@app.route('/course')
def course():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
            select * from lectures where crn = CRN
        """)
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("course.html", courseinfo=rowList)