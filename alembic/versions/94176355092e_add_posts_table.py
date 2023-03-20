"""add posts table

Revision ID: 94176355092e
Revises: 2aed9cc53a28
Create Date: 2023-03-20 12:11:15.100085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94176355092e'
down_revision = '2aed9cc53a28'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(100), nullable=False), 
                    sa.Column('content', sa.String(200), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
