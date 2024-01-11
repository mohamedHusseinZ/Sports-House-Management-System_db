"""Empty Init

Revision ID: 185cfa20c0ed
Revises: ebe989a3e64c
Create Date: 2024-01-10 04:17:36.873808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '185cfa20c0ed'
down_revision: Union[str, None] = 'ebe989a3e64c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
