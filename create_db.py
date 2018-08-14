import sqlite3 as lite
import sys
con = lite.connect('a1.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS TEMP_data")
    cur.execute("CREATE TABLE TEMP_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")