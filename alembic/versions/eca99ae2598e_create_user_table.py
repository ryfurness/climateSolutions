"""create user table

Revision ID: eca99ae2598e
Revises: 06a8cb7a7c6d
Create Date: 2020-12-11 14:30:13.188684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca99ae2598e'
down_revision = '06a8cb7a7c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
