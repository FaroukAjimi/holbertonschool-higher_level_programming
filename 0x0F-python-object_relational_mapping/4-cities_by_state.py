#!/usr/bin/python3
# now with cities
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states,cities ORDER BY states.id,cities.id ASC")
    for row in cur.fetchall():
        if row[0] == row[3]:
            print("({}, '{}', '{}')".format(row[2], row[4], row[1]))
    db.close()
