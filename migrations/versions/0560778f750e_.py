"""empty message

Revision ID: 0560778f750e
Revises: f9e22169d917
Create Date: 2022-03-05 15:34:43.252647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0560778f750e'
down_revision = 'f9e22169d917'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###