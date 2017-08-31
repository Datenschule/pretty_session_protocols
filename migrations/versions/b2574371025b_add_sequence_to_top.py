"""add_sequence_to_top

Revision ID: b2574371025b
Revises: f31e2387c73a
Create Date: 2017-08-31 11:09:21.749110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2574371025b'
down_revision = 'f31e2387c73a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tops', sa.Column('sequence', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('tops', 'sequence')
