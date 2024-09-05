"""tables

Revision ID: a178edaeb63a
Revises: c5b06e76c668
Create Date: 2024-09-05 19:36:50.204471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a178edaeb63a'
down_revision: Union[str, None] = 'c5b06e76c668'
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
