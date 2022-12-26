from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
import base64
import os

@login.user_loader
def load_user(id):
    return User.query.get(id) # already int

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique = True, nullable=False)
    password_hash = db.Column(db.String(64), nullable = False)
    gamesWon = db.Column(db.Integer, nullable = False)
    gamesPlayed = db.Column(db.Integer, nullable = False)
    moves = db.Column(db.Integer, nullable = False)
    minmoves = db.Column(db.Integer, nullable = True)
    maxmoves = db.Column(db.Integer, nullable = True)

    def to_dict(self):
        return {
            # no ID returned as this is for internal database
            # management only
            "username": self.username,
            "dateJoined": self.dateJoined,
            "score" : self.score,
            "rounds": self.rounds,
        }

    def increment_gamesWon(self):
        self.gamesWon += 1

    def increment_gamesPlayed(self):
        self.gamesPlayed += 1

    def increment_moves(self, moves):
        # check if minimum
        if self.minmoves == None and self.maxmoves == None:
            self.minmoves = moves
            self.maxmoves = moves
        elif moves > self.maxmoves:
            self.maxmoves = moves
        elif moves < self.minmoves:
            self.minmoves = moves
        self.moves += moves
            
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password):
        self.username = username
        User.set_password(self, password)
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.moves = 0
    