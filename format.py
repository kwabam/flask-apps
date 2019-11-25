import os
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g

# PostgreSQL IP address
IP_ADDR = "34.70.209.116"

# Create the application
app = Flask(__name__)


#####################################################
# Database handling

def connect_db():
    """Connects to the database."""
    debug("Connecting to DB.")
    conn = psycopg2.connect(host=IP_ADDR, user="postgres", password="rhodes", dbname="newdle",
                            cursor_factory=psycopg2.extras.DictCursor)
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
    return render_template("newdle.html")


@app.route('/home')
def home():
    return render_template("newdle2.html")


@app.route('/day')
def day():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 1
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day2')
def day2():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 2
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day3')
def day3():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 3
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day4')
def day4():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 4
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day5')
def day5():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 5
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day6')
def day6():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 6
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day7')
def day7():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 7
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day8')
def day8():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 8
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day9')
def day9():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 9
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day10')
def day10():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 10
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day11')
def day11():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 11
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day12')
def day12():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 12
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day13')
def day13():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 13
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day14')
def day14():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 14
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day15')
def day15():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 15
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day16')
def day16():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 16
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day17')
def day17():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 17
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day18')
def day18():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 18
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day19')
def day19():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 19
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day20')
def day20():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 20
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day21')
def day21():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 21
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day22')
def day22():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 22
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day23')
def day23():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 23
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day24')
def day24():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 24
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day25')
def day25():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 25
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day26')
def day26():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 26
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day27')
def day27():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 27
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day28')
def day28():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 28
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day29')
def day29():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 29
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day30')
def day30():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 30
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/day31')
def day31():
    db = get_db()
    cursor = db.cursor()
    year = "2019"
    month = "09"
    day = 31
    if day < 10:
        s_day = "0" + str(day)
    else:
        s_day = str(day)
    ymd = year + "-" + month + "-" + s_day
    cursor.execute("select * from lectures where lecturedate = '{0}'".format(ymd))
    rowList = cursor.fetchall()
    print(rowList)
    return render_template("day.html", studentinfo=rowList)


@app.route('/course', methods=['get', 'post'])
def course():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""select name from Students where name='Hannah'""")
    rowlist = cursor.fetchall()
    return render_template("newdle4.html", studentinfo=rowlist)
