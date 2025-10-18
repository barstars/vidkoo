from datetime import datetime, timedelta, date

from app.core.config import setting


def get_now_date() -> date:
	"""Return the current UTC time."""
	return datetime.utcnow().date()


def get_expires_at(days: int | None = None) -> date:
    """
    Return a date N days from now (default from settings).
    days: int | None = None
    """
    if days is None:
        days = setting.SESSION_VALIDITY_DAYS
    return get_now_date() + timedelta(days=days)