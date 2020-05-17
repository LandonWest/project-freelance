import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize Flask plugins
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Run server
# (this is an older way of doing it and `flask run` from root dir is preferred)
# if __name__ == ("__main__"):
#     app.run()
