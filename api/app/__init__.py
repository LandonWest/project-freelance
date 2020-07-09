import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Configuration
app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize Flask plugins
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Need to import at bottom of file to prevent circular imports
from app.models.user import User
from app.models.address import Address
from app.models.project import Project
from app.routes import user_routes, project_routes
