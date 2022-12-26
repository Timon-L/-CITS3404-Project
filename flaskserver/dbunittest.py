"""
python3 -m dbunittest
"""

from app import app, db
from app.models import User
from config import ConfigTest

import os, sys, random, copy

import globals

import unittest

class UserGenerator():
    
    @staticmethod
    def stringgenerator(len = 8):
        if len < 8: len = 8
        ls = []
        for i in range(len):
            ls.append(random.randrange(33, 126 + 1)) # maximum is exclusive
        return "".join(chr(j) for j in ls)

    @staticmethod
    def generateUsers(n = 100, len = 8):
        if len < 8: len = 8
        d = {}
        for i in range(n):
            # d[username] = password i.e. <username>:<password>
            d[UserGenerator.stringgenerator(random.randrange(len, len*2))] = UserGenerator.stringgenerator(random.randrange(len, len*4))
        return d


class UserTest(unittest.TestCase):
    def setUp(self):
        app.config.from_object(ConfigTest)
        self.app = app.test_client() 
        app.testing = True
        db.create_all()

    def addUsers(self, d):
        # make 2048 users with passwords ranging from 8 to 64 characters
        # (to test if the database can in fact handle very long passwords)
        assert isinstance(d, dict), f"d must be a dict but is a {type(d)}!"
        for user, plaintext_password in d.items():
            u = User(user, plaintext_password)
            db.session.add(u)
            db.session.flush()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_is_in_db(self, d, added = False):
        assert isinstance(d, dict), f"d must be a dict but is a {type(d)}!"
        for user in d.keys():
            usr = User.query.filter_by(username = user).first()
            if added: self.assertFalse(usr == None)
            else: self.assertTrue(usr == None)

    def test_password_hashed(self, d):
        assert isinstance(d, dict), f"d must be a dict but is a {type(d)}!"
        for user, plaintext_password in d.items():
            usr = User.query.filter_by(username = user).first()
            self.assertTrue(usr.check_password(plaintext_password))

    def test_score_change(self, d):
        assert isinstance(d, dict), f"d must be a dict but is a {type(d)}!"
        for user in d.keys():
            usr = User.query.filter_by(username = user).first()
            self.assertTrue(usr.gamesPlayed == usr.gamesWon == usr.moves == 0)
            # following variables check if minimum and maximum statistics are correct
            mn = None
            mx = None
            for i in range(365): 
                # test database resillience for a user that plays a game
                # each day for 1 year
                oldgw = usr.gamesWon
                oldgp = usr.gamesPlayed
                oldmv = usr.moves
                # randomly determine the moves the user makes
                newmv = random.randrange(1,65536)
                usr.increment_moves(newmv)
                if mn == None and mx == None:
                    mn = newmv
                    mx = newmv
                elif newmv > mx:
                    mx = newmv
                elif newmv < mn:
                    mn = newmv
                # randomly determine if the user won the game
                won = False
                if (random.randrange(0,2) == 1): 
                    usr.increment_gamesWon()
                    won = True
                usr.increment_gamesPlayed()
                db.session.flush()
                db.session.commit()
                self.assertTrue(usr.gamesWon - oldgw == (1 if won else 0))
                self.assertTrue(usr.gamesPlayed - oldgp == 1)
                self.assertTrue(usr.moves - oldmv == newmv)
                self.assertTrue(usr.minmoves == mn)
                self.assertTrue(usr.maxmoves == mx)

if __name__ == "__main__":
    
    n = 32
    
    # Commence unit tests
    print("Starting unit tests...")
    u = UserTest()
    u.setUp()
    print(f"Generating {n} users...", end="")
    # make 2048 users with passwords ranging from 8 to 32 characters
    d = UserGenerator.generateUsers(n, 8)
    print("OK")

    print("Testing access to database...", end = "")
    if n > 100: print("(this {0} take some time)... ".format("might" if n <= 1000 else "will"), end = "")
    u.test_is_in_db(d)
    u.addUsers(d)
    u.test_is_in_db(d, True)
    print("OK")

    print(f"Testing password hashes...", end="")
    u.test_password_hashed(d)
    print("OK")

    print(f"Testing score change...", end="")
    u.test_score_change(d)
    print("OK")
    
    # Tear down the temporary database
    u.tearDown()
    
    # Remove the temporary database
    os.remove(globals.NAMEOFDATABASE + "_test")

    os._exit(0) # success