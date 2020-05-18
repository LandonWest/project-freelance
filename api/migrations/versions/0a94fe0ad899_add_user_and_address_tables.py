"""add user and address tables

Revision ID: 0a94fe0ad899
Revises:
Create Date: 2020-05-17 19:57:45.089691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0a94fe0ad899"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("street_1", sa.String(length=80), nullable=False),
        sa.Column("street_2", sa.String(length=80), nullable=True),
        sa.Column("city", sa.String(length=80), nullable=False),
        sa.Column("state", sa.String(length=40), nullable=True),
        sa.Column("postal_code", sa.String(length=2), nullable=False),
        sa.Column("country_code", sa.String(length=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_addresses_public_id"), "addresses", ["public_id"], unique=True
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("firstname", sa.String(length=40), nullable=False),
        sa.Column("lastname", sa.String(length=40), nullable=False),
        sa.Column("company", sa.String(length=120), nullable=True),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("phone", sa.String(length=40), nullable=True),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.Column("personal_url_1", sa.String(length=120), nullable=True),
        sa.Column("personal_url_2", sa.String(length=120), nullable=True),
        sa.Column("personal_url_3", sa.String(length=120), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_public_id"), "users", ["public_id"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_users_public_id"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_addresses_public_id"), table_name="addresses")
    op.drop_table("addresses")
