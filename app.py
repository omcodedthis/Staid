
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_simple_geoip import SimpleGeoIP
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)
app.config["GEOIPIFY_API_KEY"] = "at_gE3gqT83C10hBh453MAv0VGbydDvq"
simple_geoip = SimpleGeoIP(app)



# route for home
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    else:
        return render_template("index.html")


# route for timer
@app.route("/timer", methods=["GET", "POST"])
def timer():
    if request.method == "GET":
        return render_template("timer.html")

    else:
        return render_template("timer.html")


# route for log
@app.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "GET":
        return render_template("log.html")

    else:
        return render_template("log.html")


# route for near-me
@app.route("/near-me", methods=["GET", "POST"])
def nearme():
    if request.method == "GET":
        geoip_data = simple_geoip.get_geoip_data()
        user_latitude = geoip_data["location"]["lat"]
        user_longitude = geoip_data["location"]["lng"]
        displaya = "none"

        return render_template("near-me.html", user_latitude=user_latitude, user_longitude=user_longitude, displaya=displaya)
    else:
        user_lat = float(request.form.get("lat"))
        user_lng = float(request.form.get("lng"))
        displaya = ""
        displayb = "none"
        return render_template("near-me.html", user_lat=user_lat, user_lng=user_lng, displayb=displayb, displaya=displaya)


# route for about
@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")

    else:
        return render_template("about.html")