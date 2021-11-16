"""create posts table

Revision ID: 523f04ff1c7c
Revises: 
Create Date: 2021-11-10 17:41:15.917056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
revision = '523f04ff1c7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
