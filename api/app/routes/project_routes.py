from flask import g, request

from app import app
from app.actions.project_actions import ProjectRequest
from app.routes import auth


@app.route("/api/v1/projects", methods=["POST"])
@auth.login_required
def create_project():
    project_request = ProjectRequest(user=g.user, request_json=request.json)
    return project_request.create()


@app.route("/api/v1/projects/<string:public_id>", methods=["GET"])
@auth.login_required
def retrieve_project(public_id):
    project_request = ProjectRequest(
        user=g.user, request_json=request.json, public_id=public_id
    )
    return project_request.retreive()


@app.route("/api/v1/projects", methods=["GET"])
@auth.login_required
def retrieve_projects():
    project_request = ProjectRequest(user=g.user, request_json=request.json)
    return project_request.retreive_all()


@app.route("/api/v1/projects/<string:public_id>", methods=["PUT"])
@auth.login_required
def update_project(public_id):
    project_request = ProjectRequest(request_json=request.json, public_id=public_id)
    return project_request.update


@app.route("/api/v1/projects/<string:public_id>", methods=["DELETE"])
@auth.login_required
def delete_project(public_id):
    project_request = ProjectRequest(
        user=g.user, request_json=request.json, public_id=public_id
    )
    return project_request.delete()
