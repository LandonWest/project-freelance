from datetime import datetime
import logging

from marshmallow import validate

from app.models.invoice_frequency_enum import InvoiceFrequencyEnum
from app import db, ma
from app.utils import generate_public_id


logger = logging.getLogger(__name__)


class Project(db.Model):

    __tablename__ = "projects"

    generate_project_id = generate_public_id("Project")

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(
        db.String, index=True, nullable=False, unique=True, default=generate_project_id
    )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    rate_cents = db.Column(db.Integer)
    rate_units = db.Column(db.String(10))
    completed_date = db.Column(db.DateTime)
    invoice_frequency = db.Column("invoice_frequency", db.Enum(InvoiceFrequencyEnum))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # client_id: db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # tasks: ForeignKey, List of Task
    # invoices: ForeignKey, List of Invoice

    def __repr__(self):
        return f'<Project public_id="{self.public_id}", ' + f'title="{self.title}", '


class ProjectSchema(ma.SQLAlchemySchema):
    """User Marshmallow Schema"""

    class Meta:
        model = Project

    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
    start_date = ma.auto_field()
    due_date = ma.auto_field()
    rate_cents = ma.auto_field()
    rate_units = ma.auto_field()
    completed_date = ma.auto_field()
    invoice_frequency = ma.String(
        validate=validate.OneOf("weekly" "biweekly" "monthly" "one-time" "adhoc")
    )
    user_id = ma.auto_field(dump_only=True)
