import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
#database name
dbname = "/home/pi/Assignment/PIoT_A1/a1_3.db"

#get data from database in order to display on web interface
@app.route("/")
def index():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("SELECT * FROM TEMP_data")
    data = curs.fetchall()
    templateData = {
        'data':data
    }

    return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host='0.0.0.0', port=80, debug=True)
