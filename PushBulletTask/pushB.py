import requests
import json
import os
from sense_hat import SenseHat

ACCESS_TOKEN="o.B8LbLCM0sddtHYbeE1AfL2b8vzKBOTk9"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def notify():
    sense = SenseHat()
    get_cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = float(get_cpu_temp.replace("temp=","").replace("'C\n",""))
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()

    avgtemp = (temp_h+temp_p)/2
    curr_temp = avgtemp - ((cpu_temp-avgtemp)/1.5)
    curr_temp = round(curr_temp, 1)

    if curr_temp < 20:
        send_notification_via_pushbullet("Notification", "The current temperature is " + str(curr_temp) + "*C, remember to bring a sweater!")
    elif 20<= curr_temp <= 30:
        send_notification_via_pushbullet("Notification", "The current temperature is " + str(curr_temp) + "*C, what a nice weather!")
    else:
        send_notification_via_pushbullet("Notification", "The current temperature is " + str(curr_temp) + "*C, wow it's hot today!")


def main():
    notify()
#Execute
main()
