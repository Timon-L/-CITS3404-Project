import globals

class Config(object): # Configuration object
    SQLALCHEMY_DATABASE_URI = globals.URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ConfigTest(object): # Configuration object for unit testing
    SQLALCHEMY_DATABASE_URI = globals.URI + "_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False