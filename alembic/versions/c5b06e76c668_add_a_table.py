"""Add a table

Revision ID: c5b06e76c668
Revises: 918b7ce84f33
Create Date: 2024-09-05 19:31:46.760804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5b06e76c668'
down_revision: Union[str, None] = '918b7ce84f33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
