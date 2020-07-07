from flask import g, request

from app import app
from app.actions.user_actions import UserRequest
from app.routes import auth

TOKEN_EXPIRES_IN = 3600  # 1 hour


@app.route("/api/v1/users/token", methods=["GET"])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(TOKEN_EXPIRES_IN)
    return {
        "message": "Auth token created",
        "data": {"token": token.decode("ascii"), "expires": TOKEN_EXPIRES_IN},
    }


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
