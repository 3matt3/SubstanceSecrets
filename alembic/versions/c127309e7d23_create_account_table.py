"""create account table

Revision ID: c127309e7d23
Revises: a178edaeb63a
Create Date: 2024-09-05 19:42:38.195741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c127309e7d23'
down_revision: Union[str, None] = 'a178edaeb63a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'drugs',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String)
    )


def downgrade() -> None:
    pass
