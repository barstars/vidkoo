from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid
from app.utils.time_manager import get_now_date, get_expires_at


class Sessions(Base):
    """Stores user sessions."""

    __tablename__ = "sessions"

    id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    user_id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True),ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    ip_address: Mapped[str] = mapped_column(String, nullable=False)
    client_name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(Date, default=get_now_date, nullable=False)
    expires_at: Mapped[date] = mapped_column(Date, default=get_expires_at, nullable=False)