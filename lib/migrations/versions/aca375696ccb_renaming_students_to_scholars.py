"""Renaming students to scholars

Revision ID: aca375696ccb
Revises: 791279dd0760
Create Date: 2023-08-30 22:22:49.496536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aca375696ccb'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
