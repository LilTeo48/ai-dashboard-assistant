from sqlalchemy import Column, Integer, String, Float, Date
from backend.db import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    revenue = Column(Float, nullable=False)
    sale_date = Column(Date, nullable=False)