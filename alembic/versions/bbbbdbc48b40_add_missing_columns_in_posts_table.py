"""add missing columns in posts table

Revision ID: bbbbdbc48b40
Revises: c985d5309925
Create Date: 2023-10-01 20:52:49.418515

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bbbbdbc48b40"
down_revision: Union[str, None] = "c985d5309925"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "published", sa.Boolean(), nullable=False, server_default="TRUE"
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
