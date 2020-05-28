from flask import g
from flask_httpauth import HTTPBasicAuth

from app.models.user import User


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not user.verify_password_with_hash(password):
        return False
    g.user = user
    return True


@auth.error_handler
def auth_error(status):
    return {
        'message': 'Access Denied',
        'error_fields': None
    }, status
