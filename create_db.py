import sqlite3 as lite
import sys

#connect to database
con = lite.connect('a1_3.db')

#create table
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS TEMP_data")
    cur.execute("CREATE TABLE TEMP_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")
