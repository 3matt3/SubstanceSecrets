"""create account table

Revision ID: 918b7ce84f33
Revises: 
Create Date: 2024-09-05 18:37:22.653668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '918b7ce84f33'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'drugs',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String),
    )


def downgrade() -> None:
    pass
