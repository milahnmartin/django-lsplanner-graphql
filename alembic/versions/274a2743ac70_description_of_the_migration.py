"""Description of the migration

Revision ID: 274a2743ac70
Revises: 71c3dd4f8fcc
Create Date: 2024-03-09 16:52:32.809264

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "274a2743ac70"
down_revision: Union[str, None] = "71c3dd4f8fcc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the User table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("password_hash", sa.String),
        sa.Column("date_created", sa.DateTime),
    )

    # Create the Quota table
    op.create_table(
        "api_quota",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date_created", sa.DateTime),
        sa.Column("date_updated", sa.DateTime),
        sa.Column("current_count", sa.Integer),
        sa.Column("max_count", sa.Integer),
    )


def downgrade() -> None:
    # Drop the User table
    op.drop_table("users")

    # Drop the Quota table
    op.drop_table("api_quota")
