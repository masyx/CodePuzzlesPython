import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, password_check, intTryParse

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():

    _stocksGroupedByName = db.execute("SELECT share_name, share_symbol, SUM(shares_qty) as shares_total_qty "
                                "FROM transactions WHERE user_id = ? GROUP BY share_name", session["user_id"])

    for everyDict in _stocksGroupedByName:
        if everyDict["shares_total_qty"] == 0:
            _stocksGroupedByName.remove(everyDict)

    _cash = round(db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]["cash"], 2)

    _stockPrices = {}
    for everyDict in _stocksGroupedByName:
        _stockPrices[everyDict["share_symbol"]] = lookup(everyDict["share_symbol"])["price"]

    _totalBalance = 0
    for value in _stockPrices.items():
        for row in _stocksGroupedByName:
            if row["share_symbol"] == value[0]:
                _totalBalance += value[1] * row["shares_total_qty"]

    return render_template("index.html", stocksGroupedByName = _stocksGroupedByName, cash = _cash,
                            stockPrices = _stockPrices, totalBalance = _totalBalance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":

        shares = intTryParse(request.form.get("shares")) # this is a tuple with returned true if conversion succeded and a value
        symbol = request.form.get("symbol")

        if (symbol) == "":
            return apology("must provide symbol")
        elif shares[0] < 0:
            return apology("must provide positive amount of shares")
        elif not shares[1]:
            return apology("Shares should be a number")


        #buy shares
        companyInfo = lookup(symbol)
        if companyInfo is None:
            return apology("Invalid symbol, please try again", 403)
        userInfo = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        userCash = userInfo[0]["cash"]

        # can perform transaction?
        if shares[0] * companyInfo["price"] > userCash:
            return apology("Not sufficient funds to complete transaction", 403)
        else:
            userId = userInfo[0]["id"]
            shares_qty = shares[0]
            share_price = companyInfo["price"]
            share_name = companyInfo["name"]
            share_symbol = companyInfo["symbol"]

            cashLeft = userCash - (shares_qty * companyInfo["price"])

            db.execute("INSERT INTO transactions(user_id, shares_qty, share_price, share_name, share_symbol)"
                        " VALUES(?,?,?,?,?);", userId, shares_qty, share_price, share_name, share_symbol)

            db.execute("UPDATE users SET cash = ? WHERE id = ?", cashLeft, userId)

            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    _transactions = db.execute("SELECT share_symbol, share_name, shares_qty, share_price, transaction_date "
                                "FROM transactions WHERE user_id = ?;", session["user_id"])

    _cash = round(db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]["cash"], 2)

    return render_template("history.html", transactions = _transactions, cash = _cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        username = request.form.get("username").strip()
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        _symbol = request.form.get("symbol").strip()
        _companyInfo = lookup(_symbol)
        return render_template("quoted.html", companyInfo = _companyInfo, symbol = _symbol)
    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    password = request.form.get("password")
    username = request.form.get("username")
    confirmation = request.form.get("confirmation")

    if request.method == "POST":
        # Ensure username was submitted
        if not username:
            return apology("Must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("Must provide password", 403)

        # Password validation
        if not password_check(password):
            return apology("Password should have at least one low character, one special character, "
                            "one number and have at leaset 6 characters but no more then 20.", 403)
        # Password confirmation
        if not password == confirmation:
            return apology("Passwords should match", 403)

        passwordHash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", username, passwordHash)

        return login()

    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    _symbolsOwnedStocks = []
    _stocksGroupedByName = db.execute("SELECT share_name, share_symbol, SUM(shares_qty) as shares_total_qty "
                                "FROM transactions WHERE user_id = ? GROUP BY share_name", session["user_id"])

    for everyDict in _stocksGroupedByName:
        if everyDict["shares_total_qty"] != 0:
            _symbolsOwnedStocks.append(everyDict["share_symbol"])
    #print(f"**********symbolsOwnedStocks**********: {_symbolsOwnedStocks}")

    if request.method == "POST":
        chosenStock = request.form.get("pickedStock")
        amountOfChosenStocks = int(request.form.get("stock_qty"))

        if chosenStock is None:
            return apology("Please select a share to sell", 403)
        if chosenStock not in _symbolsOwnedStocks:
            return apology(f"You do not own {chosenStock} stock", 403)

        amountOfChosenStockUserHas = (db.execute("SELECT share_name, share_symbol, SUM(shares_qty) as total_shares_qty "
                                            "FROM transactions WHERE user_id = ? AND share_symbol = ?", session["user_id"], chosenStock))[0]["total_shares_qty"]
        #print(f"**********amountOfChosenStockUserHas**********: {amountOfChosenStockUserHas}")
        if amountOfChosenStockUserHas < amountOfChosenStocks:
            return apology(f"You have only {amountOfChosenStockUserHas} of {chosenStock} shares, please choose appropriate amount", 403)


        stockName = lookup(chosenStock)["name"]
        stockPrice = lookup(chosenStock)["price"]
        #print(f"**********stockPrice**********: {stockPrice}")
        revenue = amountOfChosenStocks * stockPrice

        db.execute("INSERT INTO transactions(user_id, shares_qty, share_price, share_name, share_symbol)"
                        " VALUES(?,?,?,?,?);", session["user_id"], 0-amountOfChosenStocks, stockPrice, stockName, chosenStock)

        userInfo = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        userCash = userInfo[0]["cash"]

        newCashBalance = userCash + revenue
        db.execute("UPDATE users SET cash = ? WHERE id = ?", newCashBalance, session["user_id"])
        return redirect("/")

    else:
        return render_template("sell.html", symbolsOwnedStocks = _symbolsOwnedStocks)



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
