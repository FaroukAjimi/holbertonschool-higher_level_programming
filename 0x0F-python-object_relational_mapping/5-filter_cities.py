#!/usr/bin/python3
# filter
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    city =sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states,cities ORDER BY states.id,cities.id ASC")
    i = 0
    e = cur.fetchall()
    if len(e) == 0:
        print()
    for row in e:
        if row[0] == row[3] and city == row[1] and i == 0:
            print("{}".format(row[4]), end='')
            i = i + 1
            continue
        if row[0] == row[3] and city == row[1] and i != 0:
            print(" ,{}".format(row[4]), end='')
    print()
    db.close()
