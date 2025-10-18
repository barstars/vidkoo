from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid


class CommentsLikes(Base):
	"""Saves likes for comments."""

	__tablename__ = "comments_likes"

	id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
	user_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
	comments_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("comments.id", ondelete="CASCADE"), nullable=False)
	position: Mapped[bool] = mapped_column(Boolean, nullable=False)