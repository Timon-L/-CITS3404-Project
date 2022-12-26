from flask import render_template, request, redirect, url_for, flash, g

from app import db
from app.models import User

from utility import goodpassword

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user

class UserController():

    @staticmethod
    def logout():
        logout_user()
        flash("You have been logged out. Come back soon!", "success")
        return redirect(url_for("index"))

    @staticmethod
    def login(username, password):
        exists = User.query.filter_by(username = username).first()
        if exists:
            if exists.check_password(password):
                login_user(exists)
                return redirect(url_for("index"))
            else:
                flash(f"Incorrect password for {username}!", "failure")
        else:
            flash(f"{username} does not exist!", "failure")
        return redirect(url_for("index"))

    @staticmethod
    def signup(username, password):  
        exists = User.query.filter_by(username = username).first()
        if exists is not None: # already exists
            flash(f"User with username {username} already exists!", "failure")
        else: 
            # check password strength
            if not goodpassword(password):
                flash("Password must be eight characters long and must include uppercase and lowercase letters and a special symbol (!@#$%^&*()) !", "failure")
            else:
                # create new user
                # User class will hash the password
                myself = User(username, password)
                db.session.add(myself)
                db.session.commit()
                login_user(myself)
                flash("User account has been created and you have been logged in!", "success")
        return redirect(url_for("index")) # all POST cases: go to login

    @staticmethod 
    def updatestats(id, moves, wonThisGame):
        try:
            myself = User.query.filter_by(id = id).first()
            myself.increment_gamesPlayed()
            myself.increment_moves(moves)
            if wonThisGame: myself.increment_gamesWon()
            db.session.commit()
        except Exception as e:
            flash("Error updating: {}".format(repr(e)), "failure")
            return False
        return True
                
