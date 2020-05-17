"""initial migration

Revision ID: 16727579522d
Revises:
Create Date: 2020-05-17 14:01:16.517388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16727579522d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('public_id', sa.VARCHAR(), nullable=False),
        sa.Column('firstname', sa.VARCHAR(length=40), nullable=False),
        sa.Column('lastname', sa.VARCHAR(length=40), nullable=False),
        sa.Column('company', sa.VARCHAR(length=120), nullable=True),
        sa.Column('email', sa.VARCHAR(length=120), nullable=False),
        sa.Column('phone', sa.VARCHAR(length=40), nullable=True),
        sa.Column('password_hash', sa.VARCHAR(), nullable=False),
        sa.Column('personal_url_1', sa.VARCHAR(length=120), nullable=True),
        sa.Column('personal_url_2', sa.VARCHAR(length=120), nullable=True),
        sa.Column('personal_url_3', sa.VARCHAR(length=120), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('public_id')
    )
    op.create_table(
        'addresses',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('public_id', sa.VARCHAR(), nullable=False),
        sa.Column('street_1', sa.VARCHAR(length=80), nullable=False),
        sa.Column('street_2', sa.VARCHAR(length=80), nullable=True),
        sa.Column('city', sa.VARCHAR(length=80), nullable=False),
        sa.Column('state', sa.VARCHAR(length=40), nullable=True),
        sa.Column('postal_code', sa.VARCHAR(length=2), nullable=False),
        sa.Column('country_code', sa.VARCHAR(length=2), nullable=True),
        sa.Column('user_id', sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('public_id')
    )


def downgrade():
    op.drop_table('addresses')
    op.drop_table('users')
