import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String, nullable=False)
    content = sa.Column(sa.String, nullable=False)
    published = sa.Column(sa.Boolean, server_default="TRUE", nullable=False)
    created_at = sa.Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    email = sa.Column(sa.String, unique=True, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    # posts = relationship(Post)


class Vote(Base):
    __tablename__ = "votes"

    post_id = sa.Column(sa.Integer, sa.ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
