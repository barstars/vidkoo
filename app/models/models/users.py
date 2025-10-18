from datetime import date
from uuid import UUID as uuid_class

from sqlalchemy import String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.utils.generator import generate_uuid
from app.utils.time_manager import get_now_date

class Users(Base):
	"""Model for the 'users' table in the database."""

	__tablename__ = "users"

	id: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
	user_name: Mapped[str] = mapped_column(String(15), nullable=False)
	first_name: Mapped[str] = mapped_column(String(50), nullable=False)
	second_name: Mapped[str] = mapped_column(String(50), nullable=False)
	birthday: Mapped[date] = mapped_column(Date, nullable=False)
	emile: Mapped[str] = mapped_column(String, nullable=False)
	password_hash: Mapped[str] = mapped_column(String, nullable=False)
	profile_img_url: Mapped[uuid_class] = mapped_column(UUID(as_uuid=True), nullable=False)
	created_at: Mapped[date] = mapped_column(Date, default=get_now_date, nullable=False)