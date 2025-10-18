from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import Text, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid
from app.utils.time_manager import get_now_date


class Comments(Base):
	"""Comments for videos or replies to other comments."""

	__tablename__ = "comments"

	id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
	user_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
	video_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("videos.id", ondelete="CASCADE"), nullable=False)
	parent_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), ForeignKey("comments.id", ondelete="CASCADE"), nullable=True)
	created_at: Mapped[date] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
	comment: Mapped[str] = mapped_column(Text, nullable=False)