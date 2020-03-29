#!/usr/bin/python3
# filter
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities\
    INNER JOIN states\
    ON cities.state_id=states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC', (sys.argv[4],))
    i = 0
    z = 1
    e = cur.fetchall()
    for row in e:
        if i == 0:
            for y in range(len(e)):
                i = i + 1
        if z < i:
            print(row[0], end=", ")
            z = z + 1
            continue
        if z == i:
            print(row[0], end="")
    print()
    db.close()
