import os

NAMEOFDATABASE = "app.db"
SECRETKEY = "CITS3403-Project"

basedir = os.path.abspath(os.path.dirname(__file__))
URI = "sqlite:///{}".format(os.path.join(basedir, NAMEOFDATABASE))