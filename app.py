from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/total", methods=["POST", "GET"])
def total():
    principle = request.form.get("loan_amount")
    principle = float(principle)
    rate = request.form.get("percentage")
    rate = float(rate)
    rate = rate/100
    term = request.form.get("term")
    term = float(term)
    monthly = principle * rate / (1 - math.pow(1 + rate, - term))
    monthly = int(monthly)
    return render_template("index.html", monthly="monthly")
    








