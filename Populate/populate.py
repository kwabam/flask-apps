import psycopg2
from random import *
import csv

sample(range(100, 999), 3)

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


def main():
    con = psycopg2.connect("dbname=newdle user=kevin password=pandas300")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE Courses( CRN int PRIMARY KEY, RoomNumber int, Name varchar(50), SyllabusLink varchar(255), CoursePageLink varchar(255), Days varchar(50), startTime time, endTime time );")
    cur.execute(
        "CREATE TABLE Lectures( LectureDate date, Description varchar(255), Topic varchar(255), MaterialsLink varchar(255), CRN int REFERENCES Courses(CRN), PRIMARY KEY(LectureDate, CRN) );")

    cur.execute(
        "CREATE Table Professors( ProfessorRNumber int PRIMARY KEY, FirstName varchar(50), LastName varchar(50), OfficeHoursBegin time, OfficeHoursDuration time, OfficeNumber integer, Email varchar(50), Password varchar(255) );")
    cur.execute(
        "CREATE TABLE Students( StudentRNumber int PRIMARY KEY, FirstName varchar(50), LastName varchar(50), Email varchar(50), Password varchar(255) );")
    cur.execute(
        "CREATE TABLE Assignments( AID int PRIMARY KEY, weight float(2), description varchar(255), dueDate date, assignedDate date, title varchar(50), crn int REFERENCES Courses(crn)); ")
    cur.execute(
        "CREATE TABLE Grades( Points float(2), MaxPoints int, Category varchar(50), AID int REFERENCES Assignments(AID), StudentRNumber int REFERENCES Students(StudentRNumber), PRIMARY KEY(Points, MaxPoints, AID, StudentRNumber) );")

    f = open('Assignments.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    i = 1000
    for row in reader:
        row.insert(0, i)
        i += 1
        row[3] = fix_date(row[3])
        row[4] = fix_date(row[4])
        if not compare_date(row[3], row[4]):
            tmp = row[4]
            row[4] = row[3]
            row[3] = tmp
        cur.execute(
            "INSERT INTO Assignments VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('Courses.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    i = 1000
    for row in reader:
        row.insert(0, i)
        i += 1
        cur.execute(
            "INSERT INTO Courses VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('profs.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    i = 1000
    for row in reader:
        row.insert(0, i)
        i += 1
        cur.execute(
            "INSERT INTO Professors VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('studs.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    i = 1000
    for row in reader:
        row.insert(0, i)
        i += 1
        cur.execute(
            "INSERT INTO Students VALUES (%s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('Lecture.csv', 'r', encoding='UTF-8')
    reader = csv.reader(f)
    next(reader)
    used = []
    for row in reader:
        row[0] = fix_date(row[0])
        r = random.randint(1000, 1999)
        while r in used:
            r = random.randint(1000, 1999)
        row.append(r)
        used.append(r)
        cur.execute(
            "INSERT INTO Lectures VALUES (%s, %s, %s, %s, %s)",
            row
        )
    f.close()

    f = open('Grades.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # 34
        g1 = int(row[0])
        g2 = int(row[1])
        row[0] = str(min(g1, g2))
        row[1] = str(max(g1, g2))
        studID = random.randint(1000, 1999)
        aID = random.randint(1000, 1999)
        row.insert(3, aID)
        row.insert(4, studID)
        cur.execute(
            "INSERT INTO Grades VALUES (%s, %s, %s, %s, %s)",
            row
        )
    f.close()

    # commit changes & close
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    main()
