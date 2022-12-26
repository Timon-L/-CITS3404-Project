from utility import generaterandomnumber, generatedigit, strtobool

from app import app, models, login
from flask import request, redirect, url_for, render_template, flash, jsonify, make_response
from app.controller import UserController
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required

# ---------------------------- STANDARD FLASK -------------------------------- #
@app.route("/", methods=["GET"])
def index():
    username = "" # assume that the user is not logged in
    anon = True
    if current_user.is_authenticated: # the user is logged in
        username = current_user.username
        anon = False
    return render_template("index.html", username = username, anon = anon)

@app.route("/rules/", methods=["GET"])
def rules():
    username = "" # assume that the user is not logged in
    anon = True
    if current_user.is_authenticated: # the user is logged in
        username = current_user.username
        anon = False
    return render_template("rules.html", username = username, anon = anon)

@app.route("/stats/", methods=["GET"])
@login_required
def stats():
    return render_template("stats.html", 
        username = current_user.username, 
        anon = False, # always false since login is required
        stats = User.query.filter_by(username=current_user.username).first()
        )

# ---------------- AUTHENTICATION (FLASK_LOGIN and SQLALCHEMY)---------------- #
@app.route("/logout/", methods=["GET"])
@login_required
def logout(): return UserController.logout()

@app.route("/login/", methods=["POST"])
def handle_data_login():
    if current_user.is_authenticated:
        flash(f"You are already logged in, {current_user.username}!")
        return redirect(url_for("index"))
    else: 
        form = request.form 
        # client-side verification ensures that all fields are filled
        return UserController.login(form["username"], form["password"])


@app.route("/signup/", methods=["POST"])
def handle_data_signup():
    if current_user.is_authenticated:
        flash(f"You are already logged in, {current_user.username}!", "failure")
        return redirect(url_for("index"))
    else: 
        form = request.form
        if "agree" not in form or form["agree"] != "on":
            flash("You must agree to  Terms of Service and Privacy Policy!", "failure")
            return redirect(url_for("index"))
        # client-side verification ensures that all fields are filled
        # verify: both passwords must be the same
        if form["password"] != form["confirm-password"]:
            flash("Password fields are not identical, try again!", "failure")
            return redirect(url_for("index"))
        return UserController.signup(form["username"], form["password"])

# sending to the server: [addr]/update/?moves=[moves]won=[True or False]
@app.route("/update/", methods=["GET"])
def update():
    # current user not logged in --> do not store results
    if not current_user.is_authenticated:
        return make_response("Want to keep track of your wins? Create an account with us!", 401)
    # parameters are not correct
    if "moves" not in request.args or "won" not in request.args:
        return make_response(jsonify({"error":"Developer bug: Request does not have the required attributes"}, 500))
    # attempt to cast moves (string) into integer
    try: moves = int(request.args["moves"])
    except Exception as e: 
        return make_response(f"Developer bug: {repr(e)}", 500)
    # attempt to update the user's statistics in the database
    try:
        UserController.updatestats(current_user.id, moves, strtobool(request.args["won"]))
    except Exception as e: 
        return make_response(f"Developer bug: {repr(e)}", 500)
    return make_response("OK", 200)

# ---------------------------------------------------------------------------- #