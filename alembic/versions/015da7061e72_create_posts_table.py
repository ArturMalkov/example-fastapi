"""create posts table

Revision ID: 015da7061e72
Revises: 
Create Date: 2022-11-22 14:38:19.490388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '015da7061e72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer, nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
