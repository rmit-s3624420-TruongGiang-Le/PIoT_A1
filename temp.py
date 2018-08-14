import os
import time
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
get_cpu_temp = os.popen("vcgencmd measure_temp").readline()
cpu_temp = float(get_cpu_temp.replace("temp=","").replace("'C\n",""))
temp_h = sense.get_temperature_from_humidity()
temp_p = sense.get_temperature_from_pressure()

avgtemp = (temp_h+temp_p)/2
curr_temp = avgtemp - ((cpu_temp-avgtemp)/1.5)

sense.show_message('Current temperature is: {0:0.1f}*C'.format(curr_temp), scroll_speed=0.05)
sense.show_message('Humidity: {0:0.1f}%'.format(humidity), scroll_speed=0.05)
sense.show_message('Hay ho vl cac ong oiii', scroll_speed=0.05)

sense.clear()


