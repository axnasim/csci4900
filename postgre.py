#/usr/bin/python
#
#

import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='spdx' user='postgre' password='spdx1234'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""SELECT * from nasim.mytable""")
except:
    print "I can't SELECT from nasim.mytable"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "   ", row[1]

