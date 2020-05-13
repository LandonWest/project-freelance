from api import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # pub_id = db.Column(db.Integer, )
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    company = db.Column(db.String(120))
    street_1 = db.Column(db.String(120))
    street_2 = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    postal_code =db.Column(db.String(20))
    country_code = db.Column(db.String(2))
    personal_url_1 = db.Column(db.String(120))
    personal_url_2 = db.Column(db.String(120))
    personal_url_3 = db.Column(db.String(120))
    # photo
    # logo