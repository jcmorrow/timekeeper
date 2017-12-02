"""empty message

Revision ID: 94173d27bf8b
Revises:
    Create Date: 2017-11-28 23:18:31.624596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94173d27bf8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'work_timestamps',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            'file',
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            'time',
            sa.DateTime(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('work_timestamps')
