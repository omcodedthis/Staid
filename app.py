import json
from cs50 import SQL
from datetime import date
from flask import Flask, render_template, request
from flask_session import Session
from urllib.request import urlopen


# Configure application
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
today = date.today()
db = SQL("sqlite:///user_data.db")

# Sets API Key & URL, this is used to get user geographical data.
api_key = 'your API Key'
api_url = 'https://geo.ipify.org/api/v2/country,city?'


# route for the default page (index). The user is shown index.html, the request method of POST is not needed
# as there are no forms to be submitted.
@app.route("/", methods=["GET"])
def index():
        return render_template("index.html")


# route for timer. If the request method is via GET, timer.html is rendered with the total (total seconds for
# the countdown timer) as 0, thus, the user is shown the "00:00:00" on the page. If the request method is via
# POST, the user input is then parsed and multiplied depending on their index in the string & added to total.
# If the user inputs something in the "Session Name" textbox, the details of this session is inserted into
# user_data.db. The user is tagged using their IP address as it is unique to a user's device. If the user
# incorrectly inputs any data, error.html is shown to the user.
@app.route("/timer", methods=["GET", "POST"])
def timer():
    if request.method == "GET":
        total = 0
        return render_template("timer.html", total=total)

    else:
        try:
            duration = request.form.get("duration")

            if duration_checker(duration):
                 return render_template("error.html")

            total = 0
            total += int(duration[8] + duration[9])
            total += int(duration[4] + duration[5]) * 60
            total += int(duration[0] + duration[1]) * (60 * 60)

            user_session_name = request.form.get("session_name")
            if (len(user_session_name) > 0):
                session_date = today.strftime("%d/%m/%y")

        except ValueError:
            return render_template("error.html")

        except IndexError:
            return render_template("error.html")

        session_name = request.form.get("session_name")
        if len(session_name) > 0:
            url = api_url + 'apiKey=' + api_key + '&ipAddress=' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            response = urlopen(url)
            geoip_data = json.loads(response.read().decode('utf-8'))
            user_ip = geoip_data["ip"]
            session_date = today.strftime("%d/%m/%Y")
            db.execute("INSERT INTO user_logs (session_name, session_duration, session_date, user_ip) VALUES(?, ?, ?, ?);", session_name, duration, session_date , user_ip)

        return render_template("timer.html", total=total)


# route for logbook. If the request method is via GET, the user's sessions are retrieved from users_data.db using
# their IP as the unique identifier. The data from the SQL database is assigned to user_data which is then iterated
# over in logbook.html, showing each session as a row of the table. If the request method is via POST, the user has
# submitted the form to add their own session. This data is then added to user_data.db using their IP as the unique
# identifier. The data from the SQL database is assigned to user_data which is then iterated over in logbook.html,
# showing each session as a row of the table, including the added session. If the user incorrectly inputs any data,
# error.html is shown to the user.
@app.route("/logbook", methods=["GET", "POST"])
def logbook():
    if request.method == "GET":
        url = api_url + 'apiKey=' + api_key + '&ipAddress=' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        response = urlopen(url)
        geoip_data = json.loads(response.read().decode('utf-8'))
        user_ip = geoip_data["ip"]
        user_data = db.execute("SELECT * from user_logs WHERE user_ip = ? ORDER BY session_date DESC;", user_ip)
        return render_template("logbook.html", user_data=user_data)

    else:
        try:
            session_name = request.form.get("session_name")
            session_duration = request.form.get("session_duration")
            session_date = request.form.get("date")

            if (len(session_name) <= 0) or (len(session_duration) <= 0) or (len(session_date) <= 0):
                    return render_template("error.html")

            if duration_checker(session_duration):
                 return render_template("error.html")

            if date_checker(session_date):
                 return render_template("error.html")

            url = api_url + 'apiKey=' + api_key + '&ipAddress=' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            response = urlopen(url)
            geoip_data = json.loads(response.read().decode('utf-8'))
            user_ip = geoip_data["ip"]

            db.execute("INSERT INTO user_logs (session_name, session_duration, session_date, user_ip) VALUES(?, ?, ?, ?);", session_name, session_duration, session_date , user_ip)
            user_data = db.execute("SELECT * from user_logs WHERE user_ip = ? ORDER BY session_date DESC;", user_ip)

            return render_template("logbook.html", user_data=user_data)

        except ValueError:
                return render_template("error.html")

        except IndexError:
                return render_template("error.html")


# route for near-me. If the request method is via GET, the user's geographical details are grabbed, provided that
# their device does not block their location. This data is passed to near-me.html which then shows the map to the
# user with their coordinates. If the request method is via POST, this data is passed to near-me.html & the previous
# map is then hidden (displayb is display before map, inital map & displaya which is display after map, when requested
# via POST) & the new one is shown to the user. If the user incorrectly inputs any data, error.html is shown to the user.
@app.route("/near-me", methods=["GET", "POST"])
def nearme():
    if request.method == "GET":
        url = api_url + 'apiKey=' + api_key + '&ipAddress=' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        response = urlopen(url)
        geoip_data = json.loads(response.read().decode('utf-8'))
        user_latitude = geoip_data["location"]["lat"]
        user_longitude = geoip_data["location"]["lng"]
        displaya = "none"

        return render_template("near-me.html", user_latitude=user_latitude, user_longitude=user_longitude, displaya=displaya)
    else:
        try:
            user_lat = float(request.form.get("lat"))
            user_lng = float(request.form.get("lng"))
            if ((user_lat < -90) or (user_lat > 90) or (user_lng < -180) or (user_lng > 180)):
                return render_template("error.html")

            displaya = ""
            displayb = "none"
            return render_template("near-me.html", user_lat=user_lat, user_lng=user_lng, displayb=displayb, displaya=displaya)

        except ValueError:
            return render_template("error.html")

        except IndexError:
            return render_template("error.html")


# route for about. The user is shown about.html, the request method of POST is not needed as there are no forms to
# be submitted.
@app.route("/about", methods=["GET"])
def about():
        return render_template("about.html")


# duration_checker() checks the duration inputted follows the guidelines of 00h 00m 00s, ensuring that the duration is
# also not zero.
def duration_checker(duration):
    checker = 0
    zero_checker = 0
    for i in range(11):
        if (i == 2):
                if duration[i] == 'h':
                    checker += 1
        if (i == 6):
                if duration[i] == 'm':
                    checker += 1

        if (i == 10):
                if duration[i] == 's':
                    checker += 1

        if (i == 3) or (i == 7):
                if duration[i] == ' ':
                    checker += 1

        else:
            if duration[i].isdigit():
                    checker += 1
                    if duration[i] == '0':
                         zero_checker += 1

    if zero_checker == 6:
         return True

    if checker == 11:
        return False

    else:
         return True


# date_checker() checks the date inputted follows the guidelines of DD/MM/YYYY.
def date_checker(date):
    checker = 0
    zero_checker = 0
    for i in range(10):
        if (i == 2) or (i == 5):
            if date[i] == '/':
                checker += 1
        else:
            if date[i].isdigit():
                checker += 1
                if date[i] == '0':
                    zero_checker += 1

    if zero_checker == 8:
        return True

    if checker == 10:
        return False

    else:
         return True
