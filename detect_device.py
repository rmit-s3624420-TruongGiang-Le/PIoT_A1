#!/usr/bin/env python3
import bluetooth
import os
import time
import sqlite3
from sense_hat import SenseHat

dbname = "/home/pi/Assignment/PIoT_A1/a1_2.db"

def get_data():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    while True:
        for row in curs.execute("SELECT * FROM Device"):
            device_address = None
            nearby_devices = bluetooth.discover_devices()
            for mac_address in nearby_devices:
                if row[1] == bluetooth.lookup_name(mac_address, timeout=5):
                    device_address = mac_address
                    break
            if device_address is not None:
                print("Hi {}! Your device ({}) has the MAC address: {}".format(row[0], row[1], device_address))
                sense = SenseHat()
                get_cpu_temp = os.popen("vcgencmd measure_temp").readline()
                cpu_temp = float(get_cpu_temp.replace("temp=","").replace("'C\n",""))
                temp_h = sense.get_temperature_from_humidity()
                temp_p = sense.get_temperature_from_pressure()
                avgtemp = (temp_h+temp_p)/2
                curr_temp = avgtemp - ((cpu_temp-avgtemp)/1.5)
                temp = round(curr_temp, 1)

                humid = sense.get_humidity()
                sense.show_message("Hi {}! Current Temp is {}*c".format(row[0], temp), scroll_speed=0.05)
                sense.show_message("Current Humidity is {}%".format(round(humid, 1), ), scroll_speed=0.05)

            else:
                print("Looking for device...")
    conn.close()


# def searchdevice(user_name,device_name):
#     while True:
#         device_address = None
#         print("Looking for a nearby device, please be patient!")
#         time.sleep(5)
#         nearby_devices = bluetooth.discover_devices()

#         for mac_address in nearby_devices:
#             if device_name == bluetooth.lookup_name(mac_address, timeout=5):
#                 device_address = mac_address
#                 break
#         if device_address is not None:
#             print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
#             sense = SenseHat()

#             get_cpu_temp = os.popen("vcgencmd measure_temp").readline()
#             cpu_temp = float(get_cpu_temp.replace("temp=","").replace("'C\n",""))
#             temp_h = sense.get_temperature_from_humidity()
#             temp_p = sense.get_temperature_from_pressure()
#             avgtemp = (temp_h+temp_p)/2
#             curr_temp = avgtemp - ((cpu_temp-avgtemp)/1.5)
#             temp = round(curr_temp, 1)

#             humid = sense.get_humidity()
#             sense.show_message("Hi {}! Current Temp is {}*c".format(user_name, temp), scroll_speed=0.05)
#             sense.show_message("Current Humidity is {}%".format(round(humid, 1), ), scroll_speed=0.05)

#         else:
#             print("Could not find target device nearby...")


def main():
    get_data()
main()
