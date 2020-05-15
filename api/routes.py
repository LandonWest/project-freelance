from api.app import app, db
from api.models.address import Address
from api.models.user import User


@app.route('/')
def index():
    return {'greeting': 'Hello World!'}


@app.route('/api/v1/user', methods=['POST'])
def create_user(params=None):
    print("hitting this route")
    user_model = User(firstname='viv', 
                      lastname= 'c',
                      email='admin@gmail.com',
                      password_hash='potatos')
    db.session.add(user_model)
    db.session.commit()
    found_user = User.query.filter_by(email='admin@gmail.com').first()
    return {
        "id": found_user.id,
        "firstname": found_user.firstname,
        "lastname": found_user.lastname,
        "email": found_user.email,
    }


@app.route('/api/v1/user/<int:id>')
def lookup_user(id):
    found_user = User.query.filter_by(id=id).first()
    return {
        "id": found_user.id,
        "firstname": found_user.firstname,
        "lastname": found_user.lastname,
        "email": found_user.email,
    }
