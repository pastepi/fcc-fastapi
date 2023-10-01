"""add content column to posts table

Revision ID: 69f0ce1842c7
Revises: 793de4f96ab7
Create Date: 2023-10-01 20:39:14.570165

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "69f0ce1842c7"
down_revision: Union[str, None] = "793de4f96ab7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
