from marshmallow.exceptions import ValidationError

from app import db
from app.models.user import User, UserSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserRequest:
    """Provides methods for CRUD actions on a User resource"""

    def __init__(self, public_id=None, request_json=None):
        self.public_id = public_id
        self.request_json = request_json

    def create(self):
        try:
            req_data = user_schema.load(self.request_json)
        except ValidationError as e:
            return {"message": "invalid data passed", "error_fields": e.messages}, 422

        if User.query.filter_by(email=req_data.get("email")).first() is not None:
            return (
                {"message": "please use a different email", "error_fields": None},
                422,
            )

        user = User(
            firstname=req_data.get("firstname"),
            lastname=req_data.get("lastname"),
            company=req_data.get("company"),
            email=req_data.get("email"),
            phone=req_data.get("phone"),
            personal_url_1=req_data.get("personal_url_1"),
            personal_url_2=req_data.get("personal_url_2"),
            personal_url_3=req_data.get("personal_url_3"),
        )
        # Take in the plain text password from the client, hash it and save to User.password_hash
        user.password_hash = user.hash_password(req_data.get("password"))

        db.session.add(user)
        db.session.commit()

        return {"message": "User created", "data": user_schema.dump(user)}, 201

    def retrieve(self):
        user = User.query.filter_by(public_id=self.public_id).first()
        if not user:
            return (
                {
                    "message": f"no user found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )

        return {"message": "Success", "data": user_schema.dump(user)}, 200

    def retrieve_all(self):
        users = User.query.all()
        return {"message": "Success", "data": users_schema.dump(users)}, 200

    def update(self):
        user = User.query.filter_by(public_id=self.public_id).first()
        if not user:
            return (
                {
                    "message": f"no user found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )

        try:
            req_data = user_schema.load(self.request_json)
        except ValidationError as e:
            return {"message": "invalid data passed", "error_fields": e.messages}, 422

        user.firstname = req_data.get("firstname")
        user.lastname = req_data.get("lastname")
        user.company = req_data.get("company")
        user.email = req_data.get("email")
        user.phone = req_data.get("phone")
        user.personal_url_1 = req_data.get("personal_url_1")
        user.personal_url_2 = req_data.get("personal_url_2")
        user.personal_url_3 = req_data.get("personal_url_3")
        user.password_hash = user.hash_password(req_data.get("password"))

        db.session.commit()
        return {"message": "User updated", "data": user_schema.dump(user)}, 200

    def delete(self):
        user = User.query.filter_by(public_id=self.public_id).first()
        if not user:
            return (
                {
                    "message": f"no user found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )
        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted", "data": user_schema.dump(user)}, 200
