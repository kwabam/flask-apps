import psycopg2
import random
import csv


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

    cur.execute("""SELECT datname from pg_database""")

    #commit changes & close
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    main()