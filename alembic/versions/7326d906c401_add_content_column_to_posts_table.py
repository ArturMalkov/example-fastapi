"""add content column to posts table

Revision ID: 7326d906c401
Revises: 015da7061e72
Create Date: 2022-11-22 15:19:19.965949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7326d906c401'
down_revision = '015da7061e72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
