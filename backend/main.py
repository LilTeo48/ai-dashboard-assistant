from fastapi import FastAPI
from backend.db import SessionLocal
from backend.models import Sale

app = FastAPI()

@app.get("/")
def home(): 
    return {"message": "AI Dashboard Assistant API Running"}

@app.get("/sales")
def get_sales():
    db = SessionLocal()

    try:
        sales = db.query(Sale).all()

        return [
            {
                "id": sale.id,
                "product_name": sale.product_name,
                "category": sale.category,
                "quantity_sold": sale.quantity_sold,
                "revenue": sale.revenue,
                "sale_date": sale.sale_date,
            }
            for sale in sales 
        ]
    finally:
        db.close()        