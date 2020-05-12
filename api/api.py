from api import app, db
from api.models.user import User
from api.routes.routes import *


with app.test_request_context():
     db.init_app(app)
     db.create_all()
