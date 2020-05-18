from flask import request

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.user import User, user_schema, users_schema


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    try:
        data = user_schema.load(request.json)
    except ValidationError as e:
        return {
            "error_code": 422,
            "message": "invalid data passed",
            "error_fields": e.messages,
        }

    user = User(
        firstname=data["firstname"],
        lastname=data["lastname"],
        email=data["email"],
        password_hash="need_to_implement_this",
    )

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return {"error_code": 400, "message": str(e.__cause__), "error_fields": None}

    return {"user": user_schema.dump(user)}


@app.route("/api/v1/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return {
            "error_code": 422,
            "message": f"no user found with id {id}",
            "error_fields": None,
        }
    return {"user": user_schema.dump(user)}


@app.route("/api/v1/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return {"users": users_schema.dump(users)}
