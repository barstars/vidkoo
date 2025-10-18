from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid
from app.utils.time_manager import get_now_date


class Videos(Base):
	"""Saves data from video"""

	__tablename__ = "videos"

	id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
	user_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
	name: Mapped[str] = mapped_column(String(100), nullable=False)
	description: Mapped[str] = mapped_column(String(500), nullable=False)
	duration: Mapped[int] = mapped_column(Integer, nullable=False)
	created_at: Mapped[date] = mapped_column(Date, default=get_now_date, nullable=False)
	thumbnail_url: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), default=generate_uuid, nullable=False)