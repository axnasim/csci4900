#/usr/bin/python
#
#

import psycopg2
import sys

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

#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='spdx', user='postgre') 
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print ver    
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
