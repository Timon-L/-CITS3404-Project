import globals
# FLASK IMPORT
from flask import Flask
# DATABASE (SQLALCHEMY IMPORTS)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# AUTHENTICATION
from flask_login import LoginManager
# --------------------------------------------------------------------------- #

# Create Flask app
app = Flask(__name__)

# Configure secret key
app.config["SECRET_KEY"] = globals.SECRETKEY

# ----------------------------- AUTHENTICATION ------------------------------ #

login = LoginManager(app)
login.login_view = "index"
login.login_message = "Please log in to access this page." # default message
login.login_message_category = "failure"

# ------------------------- DATABASE INITIALISATION ------------------------- #
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.models import User
migrate = Migrate(app, db)
db.create_all()

# --------------------------------------------------------------------------- #
from app import routes