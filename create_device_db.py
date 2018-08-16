import sqlite3 as lite
import sys
con = lite.connect('a1.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS Device")
    cur.execute("CREATE TABLE Device(timestamp DATETIME, user_name CHARACTER, device_name CHARACTER, MAC_add CHARACTER)")
