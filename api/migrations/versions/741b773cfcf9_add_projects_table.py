"""add Projects table

Revision ID: 741b773cfcf9
Revises: 0a94fe0ad899
Create Date: 2020-06-26 00:15:38.856178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "741b773cfcf9"
down_revision = "0a94fe0ad899"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "Projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_Projects_public_id"), "Projects", ["public_id"], unique=True
    )


def downgrade():
    op.drop_index(op.f("ix_Projects_public_id"), table_name="Projects")
    op.drop_table("Projects")
