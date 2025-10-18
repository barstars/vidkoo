from pydantic_settings import BaseSettings

class Setting(BaseSettings):
	"""
	Config datas
	"""
	SESSION_VALIDITY_DAYS: int

	class Config:
		env_file = ".env"

setting = Setting()