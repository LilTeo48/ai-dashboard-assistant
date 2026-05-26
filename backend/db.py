from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///sales.db"

engine = create_engine(DATABASE_URL)