from api.app import db, ma
from api.utils import generate_public_id


class Address(db.Model):
    """Address model and db class"""

    __tablename__ = "addresses"

    generate_address_id = generate_public_id("Address")

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(
        db.String, index=True, nullable=False, unique=True, default=generate_address_id
    )
    street_1 = db.Column(db.String(80), nullable=False)
    street_2 = db.Column(db.String(80))
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(40))
    postal_code = db.Column(db.String(2), nullable=False)
    country_code = db.Column(db.String(2), default="US")

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", backref=db.backref("addresses"))

    def __repr__(self):
        return (
            f'<User public_id="{self.public_id}", '
            + f'street_1="{self.street_1}", '
            + f'street_2="{self.street_2}", '
            + f'city="{self.city}", '
            + f'state="{self.state}", '
            + f'postal_code="{self.postal_code}", '
            + f'country_code="{self.country_code}"'
        )
