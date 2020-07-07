import logging
import os
import time

import jwt

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, ma
from app.models.project import Project
from app.utils import generate_public_id

logger = logging.getLogger(__name__)


class User(db.Model):
    """User class / db model"""

    generate_user_id = generate_public_id("User")

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(
        db.String, index=True, nullable=False, unique=True, default=generate_user_id
    )
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(40))
    personal_url_1 = db.Column(db.String(120))
    personal_url_2 = db.Column(db.String(120))
    personal_url_3 = db.Column(db.String(120))
    password_hash = db.Column(db.String(128), nullable=False)
    projects = db.relationship("Project", backref="users", lazy=True)

    # address = db.relationship("Address", uselist=False, backref=db.backref("users"))
    # photo
    # logo

    def __repr__(self):
        return (
            f'<User public_id="{self.public_id}", '
            + f'firstname="{self.firstname}", '
            + f'lastname="{self.lastname}", '
            + f'company="{self.company}", '
            + f'email="{self.email}", '
            + f'phone="{self.phone}", '
            + f'personal_url_1="{self.personal_url_1}", '
            + f'personal_url_2="{self.personal_url_2}", '
            + f'personal_url_3="{self.personal_url_3}"'
        )

    def hash_password(self, password):
        """Uses werkzeug to hash the plaintext password
        Sets the password_hash as a property of the User
        """
        logger.debug("hashing password...")
        self.password_hash = generate_password_hash(password, method="sha256")

    def verify_password_with_hash(self, password):
        """Uses werkzeug to check the password_hash against the plaintext password.
        Returns `True` if the password matched, `False` otherwise.
        """
        logger.debug("verifying password with hash...")
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):  # 600 seconds == 10 minutes :)
        """Uses PyJWT to generate and return a json web token hash.
        ex: {'id': '3a2f4d24-8523-432d-87c3-50c8dddf74ff-usr', 'exp': 1590707818.466217}
        """
        logger.debug("generating an auth token...")
        payload = jwt.encode(
            {"id": self.public_id, "exp": time.time() + expires_in},
            os.environ["FLASK_SECRET_KEY"],
            algorithm="HS256",
        )
        return payload

    @staticmethod
    def verify_auth_token(token):
        logger.debug("attempting to verify auth token...")
        try:
            data = jwt.decode(
                token, os.environ["FLASK_SECRET_KEY"], algorithms=["HS256"]
            )
        except jwt.exceptions.ExpiredSignatureError:
            logger.warn("auth token expired: ")
            return
        except ValueError:
            logger.error("malformed auth token: ")
            return

        user = User.query.filter_by(public_id=data["id"]).first()
        return user


def validate_password_constraints(password):
    if len(password) < 8:
        raise ma.ValidationError("Password must be at least 8 characters long")


class UserSchema(ma.SQLAlchemySchema):
    """User Marshmallow Schema"""

    class Meta:
        model = User

    exclude = "password_hash"

    public_id = ma.auto_field()
    firstname = ma.auto_field()
    lastname = ma.auto_field()
    company = ma.auto_field()
    email = ma.Email(required=True)
    phone = ma.auto_field()
    personal_url_1 = ma.URL()
    personal_url_2 = ma.URL()
    personal_url_3 = ma.URL()
    password = ma.String(
        required=True, validate=validate_password_constraints, load_only=True
    )
    projects = ma.auto_field()
    # addresses = ma.auto_field()
