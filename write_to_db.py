#!/usr/bin/env python3

import time
import os
import sqlite3
from sense_hat import SenseHat
dbname='/home/pi/Assignment/PIoT_A1/a1_3.db'
sense = SenseHat()
sense.show_message("Recording data", scroll_speed=0.05)

# get data from SenseHat sensor
def getSenseHatData():	
    
    humidity = sense.get_humidity()
    get_cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = float(get_cpu_temp.replace("temp=","").replace("'C\n",""))
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()

    #calculate the correct temperature from the sense hat
    avgtemp = (temp_h+temp_p)/2
    curr_temp = avgtemp - ((cpu_temp-avgtemp)/1.5)

	
    if curr_temp is not None:
        curr_temp = round(curr_temp, 1)
        humidity = round(humidity, 1)
        logData (curr_temp, humidity)

# log sensor data on database
def logData (curr_temp, humidity):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO TEMP_data values(datetime('now','localtime'), (?), (?))", (curr_temp, humidity,))
    conn.commit()
    conn.close()



# main function
def main():
    getSenseHatData()
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    print ("(date                 ,tem,humid)")
    for row in curs.execute("SELECT * FROM TEMP_data"):
        print (row)
    conn.close()
# Execute program 
main()
