import sqlite3 as lite
import sys

#connect to database
con = lite.connect('a1_2.db')

#create table
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS Device")
    cur.execute("CREATE TABLE Device(user_name CHARACTER, device_name CHARACTER)")
