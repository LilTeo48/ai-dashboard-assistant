from backend.db import Base, engine
from backend.models import Sale 

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")