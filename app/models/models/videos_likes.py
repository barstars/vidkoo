from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid


class VideosLikes(Base):
	"""Saves likes for videos."""

	__tablename__ = "videos_likes"

	id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
	user_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
	video_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)
	position: Mapped[bool] = mapped_column(Boolean, nullable=False)