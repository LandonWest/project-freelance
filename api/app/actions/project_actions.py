from marshmallow.exceptions import ValidationError

from app import db
from app.models.project import Project, ProjectSchema


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)


class ProjectRequest:
    """Provides methods for CRUD actions on a Project resource"""

    def __init__(self, user, public_id=None, request_json=None):
        self.public_id = public_id
        self.request_json = request_json
        self.user = user

    def create(self):
        try:
            req_data = project_schema.load(self.request_json)
        except ValidationError as e:
            return {"message": "invalid data passed", "error_fields": e.messages}, 422

        project = Project(
            title=req_data.get("title"),
            description=req_data.get("description"),
            start_date=req_data.get("start_date"),
            due_date=req_data.get("due_date"),
            rate_cents=req_data.get("rate_cents"),
            rate_units=req_data.get("rate_units"),
            completed_date=req_data.get("completed_date"),
            invoice_frequency=req_data.get("invoice_frequency"),
            user_id=self.user.id,
        )

        try:
            db.session.add(project)
            db.session.commit()
        except Exception as e:
            print(e)
            return {"message": "There was a database error", "error_fields": None}, 500

        return {"message": "Project created", "data": project_schema.dump(project)}, 201

    def retrieve(self):
        project = Project.query.filter_by(
            user_id=self.user.id, public_id=self.public_id
        ).first()
        if not project:
            return (
                {
                    "message": f"no project found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )

        return {"message": "Success", "data": project_schema.dump(project)}, 200

    def retrieve_all(self):
        projects = Project.query.filter_by(user_id=self.user.id).all()
        return {"message": "Success", "data": projects_schema.dump(projects)}, 200

    def update(self):
        project = Project.query.filter_by(public_id=self.public_id).first()
        if not project:
            return (
                {
                    "message": f"no project found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )

        try:
            req_data = project_schema.load(self.request_json)
        except ValidationError as e:
            return {"message": "invalid data passed", "error_fields": e.messages}, 422

        project.title = req_data.get("title")
        project.description = req_data.get("description")
        project.start_date = req_data.get("start_date")
        project.due_date = req_data.get("due_date")
        project.rate_cents = req_data.get("rate_cents")
        project.rate_units = req_data.get("rate_units")
        project.completed_date = req_data.get("completed_date")
        project.invoice_frequency = req_data.get("invoice_frequency")

        db.session.commit()
        return {"message": "project updated", "data": project_schema.dump(project)}, 200

    def delete(self):
        project = Project.query.filter_by(
            user_id=self.user.id, public_id=self.public_id
        ).first()
        if not project:
            return (
                {
                    "message": f"no project found with id {self.public_id}",
                    "error_fields": None,
                },
                404,
            )
        db.session.delete(project)
        db.session.commit()

        return {"message": "Project deleted", "data": project_schema.dump(project)}, 200
