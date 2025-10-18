from datetime import datetime, timedelta, date

def get_now_date() -> date:
	"""Getting the current UTC time."""
	return datetime.utcnow().date()


def get_expires_at(days=30) -> date:
	"""Return a date N days from now"""
	return (get_now_date() + timedelta(days=days))