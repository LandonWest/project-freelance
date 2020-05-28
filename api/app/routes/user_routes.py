from flask import request

from app import app
from app.actions.user_actions import UserRequest
from app.routes import auth


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    user_request = UserRequest(request_json=request.json)
    return user_request.create()


@app.route("/api/v1/users/<string:public_id>", methods=["GET"])
@auth.login_required
def retrieve_user(public_id):
    user_request = UserRequest(public_id=public_id)
    return user_request.retrieve()


@app.route("/api/v1/users", methods=["GET"])
@auth.login_required
def retrieve_users():
    user_request = UserRequest()
    return user_request.retrieve_all()


@app.route("/api/v1/users/<string:public_id>", methods=["PUT"])
@auth.login_required
def update_user(public_id):
    user_request = UserRequest(public_id=public_id, request_json=request.json)
    return user_request.update()


@app.route("/api/v1/users/<string:public_id>", methods=["DELETE"])
@auth.login_required
def delete_user(public_id):
    user_request = UserRequest(public_id=public_id)
    return user_request.delete()
