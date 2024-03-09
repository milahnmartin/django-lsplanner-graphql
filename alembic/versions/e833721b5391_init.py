"""init

Revision ID: e833721b5391
Revises:
Create Date: 2024-03-09 18:20:15.739386

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e833721b5391"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("password", sa.String),
        sa.Column(
            "date_created", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
    )

    op.create_table(
        "api_quota",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "date_created", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.Column(
            "date_updated",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.Column("current_count", sa.Integer, nullable=False),
        sa.Column("max_count", sa.Integer, nullable=False),
    )

    # Add additional operations as needed


# Downgrade function
def downgrade():
    op.drop_table("api_quota")
    op.drop_table("users")
