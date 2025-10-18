import uuid

def generate_uuid() -> uuid.UUID:
	'''Generate a new UUID4 object.'''
	return uuid.uuid4()