"""add projects table

Revision ID: a8e960943ccf
Revises: 0a94fe0ad899
Create Date: 2020-07-07 22:40:40.409672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a8e960943ccf"
down_revision = "0a94fe0ad899"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("start_date", sa.DateTime(), nullable=True),
        sa.Column("due_date", sa.DateTime(), nullable=True),
        sa.Column("rate_cents", sa.Integer(), nullable=True),
        sa.Column("rate_units", sa.String(length=10), nullable=True),
        sa.Column("completed_date", sa.DateTime(), nullable=True),
        sa.Column(
            "invoice_frequency",
            sa.Enum(
                "weekly",
                "biweekly",
                "monthly",
                "one_time",
                "adhoc",
                name="invoicefrequencyenum",
            ),
            nullable=True,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_projects_public_id"), "projects", ["public_id"], unique=True
    )


def downgrade():
    op.drop_index(op.f("ix_projects_public_id"), table_name="projects")
    op.drop_table("projects")
