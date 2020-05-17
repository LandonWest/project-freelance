from api.app import db, ma
from api.utils import generate_public_id


class User(db.Model):
    """User model and db class"""

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
    password_hash = db.Column(db.String, nullable=False)
    personal_url_1 = db.Column(db.String(120))
    personal_url_2 = db.Column(db.String(120))
    personal_url_3 = db.Column(db.String(120))

    address = db.relationship("Address", uselist=False, backref=db.backref("users"))
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
