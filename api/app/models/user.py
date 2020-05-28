from passlib.apps import custom_app_context as pwd_context

from app import db, ma
from app.utils import generate_public_id


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
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


def validate_password_constraints(password):
    if len(password) < 8:
        raise ma.ValidationError("Password must be at least 8 characters long")


class UserSchema(ma.SQLAlchemySchema):
    """User Marshmallow Schema"""

    class Meta:
        model = User

    exclude = ("password_hash")

    public_id = ma.auto_field()
    firstname = ma.auto_field()
    lastname = ma.auto_field()
    company = ma.auto_field()
    email = ma.Email(required=True)
    phone = ma.auto_field()
    personal_url_1 = ma.URL()
    personal_url_2 = ma.URL()
    personal_url_3 = ma.URL()
    password = ma.String(required=True, validate=validate_password_constraints, load_only=True)
    # addresses = ma.auto_field()
