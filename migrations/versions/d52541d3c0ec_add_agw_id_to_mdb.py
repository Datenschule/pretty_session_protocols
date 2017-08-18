"""add agw id to mdb

Revision ID: d52541d3c0ec
Revises: e93ed69447d8
Create Date: 2017-08-15 16:33:05.537925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd52541d3c0ec'
down_revision = 'e93ed69447d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mdb', sa.Column('agw_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mdb', 'agw_id')
    # ### end Alembic commands ###
