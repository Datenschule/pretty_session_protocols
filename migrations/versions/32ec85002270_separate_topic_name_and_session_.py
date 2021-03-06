"""separate topic name and session identifier

Revision ID: 32ec85002270
Revises: b2574371025b
Create Date: 2017-09-03 18:09:12.678823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ec85002270'
down_revision = 'b2574371025b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tops', sa.Column('name', sa.String(), nullable=True))
    op.add_column('tops', sa.Column('session_identifier', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tops', 'session_identifier')
    op.drop_column('tops', 'name')
    # ### end Alembic commands ###
