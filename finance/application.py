from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import datetime

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.globals.update(usd=usd, lookup=lookup)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@app.route("/index")
@login_required
def index():
    person = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"])
    user_history = db.execute("SELECT stock_name, price, SUM(shares) AS total_shares FROM history WHERE user_id = :user GROUP BY stock_name", user=session["user_id"])
    current_cash = (db.execute("SELECT cash FROM users WHERE id = :current_user", current_user=session["user_id"]))[0]['cash']
    # for stock in user_history:
    #     if stock['stock_name']

    # current_price = lookup()
    # total = number_of_shares
    message = "Hello, {}. Here are your holdings:".format(person[0]['username'])
    return render_template("index.html", person=person, message=message, user_history=user_history, current_cash=current_cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    """Buy shares of stock."""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":

        # set inputs as variables
        new_shares = int(request.form.get("shares"))
        stock = lookup(request.form.get("stock_to_buy"))
        print(stock)
        print(new_shares)

        # make sure inputs given and valid
        if not stock or new_shares <= 0:
            return apology("Sorry, please input a stock symbol and amount of shares")

        current_cash = (db.execute("SELECT cash FROM users WHERE id = :current_user", current_user=session["user_id"]))[0]['cash']

        if current_cash > stock['price']*new_shares:
            time = str(datetime.datetime.now())
            new_cash = current_cash - stock['price']*new_shares
            db.execute("INSERT INTO history (stock_name, timestamp, shares, price, user_id) VALUES(:stock, :time, :shares, :price, :user)", stock=stock['name'], time=time, shares=new_shares, price=stock['price'], user=session['user_id'])
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=new_cash, user_id=session['user_id'])

        else:
            return apology("Sorry, you don't have enough money!")

    # redirect user to home page
    return redirect(url_for("index"))

@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():

    """Buy shares of stock."""
    if request.method == "GET":
        return render_template("deposit.html")

    if request.method == "POST":
        if not request.form.get("deposit").isnumeric():
            return apology("Please only user numeric values for deposit amount")
        deposit = int(request.form.get("deposit"))
        print(deposit)
        if not deposit:
            return apology("You must enter a numerical amount to deposit")

        old_cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])[0]['cash']
        print(old_cash)
        new_cash = deposit + old_cash
        print(new_cash)
        db.execute("UPDATE users SET cash = :new_cash WHERE id=:user_id", new_cash=new_cash, user_id=session["user_id"])
        return redirect(url_for("index"))

@app.route("/history")
@login_required
def history():
    person = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=session["user_id"])
    user_history = db.execute("SELECT * FROM history WHERE user_id = :user", user=session["user_id"])
    current_cash = (db.execute("SELECT cash FROM users WHERE id = :current_user", current_user=session["user_id"]))[0]['cash']
    message = "Hello, {}. Here is your transaction history:".format(person[0]['username'])
    return render_template("history.html", message=message, user_history=user_history, current_cash=current_cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    if request.method == "POST":

        stock = lookup(request.form.get("stock"))
        if not stock:
            return apology("Sorry, stock does not exist")
        return render_template("quoted.html", stock=stock)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    session.clear()

    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")
        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        # ensure password confirmation matches
        elif request.form.get("password_conf") != request.form.get("password"):
            return apology("password confirmation does not match password")
        # hash password
        hash_pw = pwd_context.encrypt(request.form.get("password"))
        # add user to database
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash_pw)", username=request.form.get("username"), hash_pw=hash_pw)
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        if not rows:
            return apology("Sorry, there was a problem, maybe username or password already exists")
        else:
            session["user_id"] = rows[0]["id"]
            # redirect user to home page
            return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method == "GET":
        return render_template("sell.html")

    if request.method == "POST":

        # set user input as variables
        stock_to_sell = db.execute("SELECT stock_name, SUM(shares) AS sum_shares FROM history WHERE user_id = :user AND stock_name = :stock_name GROUP BY stock_name", stock_name=request.form.get("stock_to_sell"), user=session["user_id"])[0]
        shares_to_sell = int(request.form.get("shares"))

        # error check
        if not stock_to_sell or not shares_to_sell:
            return apology("Please input a correct stock symbol (that you own) and number of shares")
        elif stock_to_sell['sum_shares'] < shares_to_sell:
            return apology("You don't have that many shares to sell")
        else:
            # delete stock shares from user and add money back to account
            time = str(datetime.datetime.now())
            new_price = lookup(stock_to_sell['stock_name'])['price']
            user_cash = db.execute("SELECT cash FROM users WHERE id=:user", user=session["user_id"])[0]['cash']
            print(user_cash)
            proceeds = user_cash + new_price*shares_to_sell
            new_shares = stock_to_sell['sum_shares'] - shares_to_sell
            db.execute("UPDATE users SET cash = :cash WHERE id=:user_id", cash=proceeds, user_id=session["user_id"])
            db.execute("INSERT INTO history (stock_name, timestamp, shares, price, user_id) VALUES(:stock, :time, :shares, :price, :user)", stock=stock_to_sell['stock_name'], time=time, shares= -shares_to_sell, price=new_price, user=session['user_id'])
            return redirect(url_for('index'))


