#!/usr/bin/python3
# sql injection safe
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    state = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        if row[1] in state:
            print("({}, '{}')".format(row[0], row[1]))
    db.close()
