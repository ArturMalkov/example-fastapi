"""add foreign key to posts table

Revision ID: b573b70ca6a8
Revises: 1e3a1f1458a4
Create Date: 2022-11-22 16:03:42.701520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b573b70ca6a8'
down_revision = '1e3a1f1458a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer, nullable=False))
    op.create_foreign_key("post_users_fk",
                          source_table="posts",
                          referent_table="users",
                          local_cols=["user_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "user_id")
