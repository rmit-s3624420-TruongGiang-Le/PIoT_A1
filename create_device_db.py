import sqlite3 as lite
import sys
con = lite.connect('a1_2.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS Device")
    cur.execute("CREATE TABLE Device(user_name CHARACTER, device_name CHARACTER)")
