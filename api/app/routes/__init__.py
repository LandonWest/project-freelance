import logging

from flask import g
from flask_httpauth import HTTPBasicAuth
from jwt.exceptions import DecodeError

from app.models.user import User


auth = HTTPBasicAuth()
logger = logging.getLogger(__name__)


@auth.verify_password
def verify_password(username_or_token, password):
    # Try to authenticate via auth token first
    logger.debug('trying to authenticate with token...')
    try:
        user = User.verify_auth_token(username_or_token)
    except DecodeError:
        user = None

    if not user:
        # If token method didn't work try to authenticate with email/password
        logger.debug('trying to authenticate with password...')
        user = User.query.filter_by(email=username_or_token).first()

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
