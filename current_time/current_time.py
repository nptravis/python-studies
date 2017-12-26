from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
	now = datetime.now(timezone('America/New_York'))
	return "The current date and time in NYC is {}".format(now)
