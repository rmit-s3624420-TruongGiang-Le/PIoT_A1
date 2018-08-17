import os
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/Assignment/PIoT_A1/a1_2.db'

user_name = input("Please enter your name: ")
device_name = input("Please enter your device's name: ")

def logData (user_name, device_name):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO Device values((?), (?))", (user_name, device_name,))
    conn.commit()
    conn.close()

def main():
    logData(user_name, device_name)
    sense = SenseHat()
    sense.show_message("Data recorded!", scroll_speed=0.05)

main()
