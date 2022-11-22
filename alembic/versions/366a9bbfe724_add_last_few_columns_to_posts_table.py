"""add last few columns to posts table

Revision ID: 366a9bbfe724
Revises: b573b70ca6a8
Create Date: 2022-11-22 16:16:06.930768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '366a9bbfe724'
down_revision = 'b573b70ca6a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean, server_default="TRUE", nullable=False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"),
                                     nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
