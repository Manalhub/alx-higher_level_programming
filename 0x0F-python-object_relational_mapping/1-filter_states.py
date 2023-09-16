#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    [print(state) for state in cur.fetchall()]

    cur.close()
    db.close()

#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    states = cur.fetchall()
    for i in states:
        print(i)
    # Clean up process
    cur.close()
    db.close()
