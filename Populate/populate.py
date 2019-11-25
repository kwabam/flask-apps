import psycopg2
from random import *
import csv
from essential_generators import *

classes = []
with open('classes.txt', 'r') as f:
    for line in f:
        classes.append(line.rstrip())

def fix_date(s):
    d = s.split(".")
    t = d[0]
    d[0] = d[2]
    d[2] = t
    return "-".join(d)


def compare_date(d1, d2):
    d1 = d1.split('-')
    d2 = d2.split('-')
    d1 = [int(c) for c in d1]
    d2 = [int(c) for c in d2]
    if d2[0] < d1[0]:
        return 1
    if d2[0] > d1[0]:
        return 0
    if d2[1] < d1[1]:
        return 1
    if d2[1] > d1[1]:
        return 0
    if d2[2] < d1[2]:
        return 1
    return 0

def find_hm(t):
    h, m = t.split(':')
    h = int(h)
    m, am = m.split(' ')
    m = int(m)
    if am == 'PM' and h != 12:
        h += 12
    return h, m
def compare_time(t1, t2):
    h1, m1  = find_hm(t1)
    h2, m2 = find_hm(t2)
    if h1 < h2:
        return t1, t2
    if h1 > h2:
        return t2, t1
    if h1 == h2:
        if m1 < m2:
            return t1, t2
        return t2, t1


def main():
    gen = DocumentGenerator()
    con = psycopg2.connect("dbname=newdle user=kevin password=pandas300")
    cur = con.cursor()
    cur.execute("""
        DROP SCHEMA public CASCADE;
        CREATE SCHEMA public;
        GRANT ALL ON SCHEMA public TO postgres;
        GRANT ALL ON SCHEMA public TO public;
        COMMENT ON SCHEMA public IS 'standard public schema';
    """)
    cur.execute(
        "CREATE TABLE Courses( CRN int PRIMARY KEY, RoomNumber int, Name varchar(50), SyllabusLink varchar(255), CoursePageLink varchar(255), Days varchar(50), startTime time, endTime time );")
    cur.execute(
        "CREATE TABLE Lectures( LectureDate date, Description varchar(1024), Topic varchar(255), MaterialsLink varchar(255), CRN int REFERENCES Courses(CRN), PRIMARY KEY(LectureDate, CRN) );")

    cur.execute(
        "CREATE Table Professors( ProfessorRNumber int PRIMARY KEY, FirstName varchar(50), LastName varchar(50), OfficeHoursBegin time, OfficeHoursDuration time, OfficeNumber integer, Email varchar(50), Password varchar(255) );")
    cur.execute(
        "CREATE TABLE Students( StudentRNumber int PRIMARY KEY, FirstName varchar(50), LastName varchar(50), Email varchar(50), Password varchar(255) );")
    cur.execute(
        "CREATE TABLE Assignments( AID int PRIMARY KEY, description varchar(255), dueDate date, assignedDate date, title varchar(50), crn int REFERENCES Courses(crn)); ")
    cur.execute(
        "CREATE TABLE Grades( Points float(2), MaxPoints int, AID int REFERENCES Assignments(AID), StudentRNumber int REFERENCES Students(StudentRNumber), PRIMARY KEY(Points, MaxPoints, AID, StudentRNumber) );")
    cur.execute(
        "CREATE TABLE Enrolled( StudentRNumber int REFERENCES Students(StudentRNumber), CRN int REFERENCES Courses(CRN), PRIMARY KEY(StudentRNumber, CRN) );")

    f = open('Courses.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    CRNS = sample(range(10000,99999), 20)
    for (i, row) in enumerate(reader):
        if i >= 20:
            break
        row.insert(0, CRNS[i])
        row[2] = classes[i]
        row[3] = row[3] + "/syllabus/" + str(row[0])
        row[4] = row[4] + "/course/" + str(row[0])

        row[6], row[7] = compare_time(row[6], row[7])

        cur.execute(
            "INSERT INTO Courses VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('Assignments.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    AIDS = sample(range(10000, 99999), 200)
    for (i, row) in enumerate(reader):
        if i >= 200:
            break
        row.insert(0, AIDS[i])
        i += 1
        row[3] = fix_date(row[3])
        row[4] = fix_date(row[4])
        if not compare_date(row[3], row[4]):
            tmp = row[4]
            row[4] = row[3]
            row[3] = tmp
        row.pop(1)
        row.append(choice(CRNS))
        cur.execute(
            "INSERT INTO Assignments VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('profs.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    PIDS = sample(range(100000, 999999), 10)
    for (i, row) in enumerate(reader):
        if i >= 10:
            break
        row.insert(0, PIDS[i])
        row[3], row[4] = compare_time(row[3], row[4])
        cur.execute(
            "INSERT INTO Professors VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()
    SIDS = sample(range(100000, 999999), 100)
    f = open('studs.csv', 'r')
    reader = csv.reader(f)
    next(reader)

    for (i, row) in enumerate(reader):
        if i >= 100:
            break
        row.insert(0, SIDS[i])
        cur.execute(
            "INSERT INTO Students VALUES (%s, %s, %s, %s, %s)",
            row
        )
    f.close()


    # f = open('Lecture.csv', 'r', encoding='UTF-8')
    # reader = csv.reader(f)
    # next(reader)
    # used = []
    #
    # exit(1)
    # for (i, row) in enumerate(reader):
    #     if i >= 600:
    #         break
    #     row[0] = fix_date(row[0])
    #     r = randint(1000, 1999)
    #     row.append(r)
    #     used.append(r)
    #     cur.execute(
    #         "INSERT INTO Lectures VALUES (%s, %s, %s, %s, %s)",
    #         row
    #     )
    # f.close()

    for i in range(len(classes)):
        for j in range(30):
            row = []
            month = "09"
            if j <= 10:
                day = "0" + str(j+1)
            else:
                day = str(j+1)
            year = "2019"
            ymd = year + "-" + month + "-" + day

            topic = gen.sentence()
            description = gen.paragraph(min_sentences=2, max_sentences=3)
            link = "www.newdle.rhodes.edu/lecture/?date=" + ymd + "?CRN=" + str(CRNS[i])
            row = [ymd, description, topic, link, CRNS[i]]
            cur.execute(
                "INSERT INTO Lectures VALUES (%s, %s, %s, %s, %s)",
                row
            )
    enrolled = []
    for s in SIDS:
        schedule = sample(CRNS, 4)
        for crn in schedule:
            row = [s, crn]
            enrolled.append(row)
            cur.execute(
                "INSERT INTO Enrolled VALUES (%s, %s)",
                row
            )

    for s in enrolled:
        sid = s[0]
        crn = s[1]
        cur.execute("select AID from Assignments where CRN = '{0}'"\
                    .format(crn))
        rows = cur.fetchall()
        for row in rows:
            a = row[0]
            maxpoints = 5*randint(1,20)
            points = randint(0,maxpoints)
            grade_row = [points, maxpoints, a, sid]
            cur.execute(
                "INSERT INTO Grades VALUES (%s, %s, %s, %s)",
                grade_row
            )

    # commit changes & close
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    main()
