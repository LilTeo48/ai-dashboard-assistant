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


@app.get("/sales/top-products")
def get_top_products():
    db = SessionLocal()

    try:
        sales = db.query(Sale).all()

        sorted_sales = sorted(
            sales,
            key=lambda sale: sale.revenue,
            reverse=True
        )

        return [
            {
                "product_name": sale.product_name,
                "category": sale.category,
                "revenue": sale.revenue,
                "quantity_sold": sale.quantity_sold,
            }
            for sale in sorted_sales
        ]

    finally:
        db.close()


@app.get("/sales/categories")
def get_category_summary():
    db = SessionLocal()

    try:
        sales = db.query(Sale).all()

        summary = {}

        for sale in sales:
            if sale.category not in summary:
                summary[sale.category] = {
                    "total_revenue": 0,
                    "total_quantity_sold": 0
                }

            summary[sale.category]["total_revenue"] += sale.revenue
            summary[sale.category]["total_quantity_sold"] += sale.quantity_sold

        return summary

    finally:
        db.close()


@app.get("/sales/summary")
def get_sales_summary():
    db = SessionLocal()

    try:
        sales = db.query(Sale).all()

        total_revenue = sum(sale.revenue for sale in sales)
        total_quantity_sold = sum(sale.quantity_sold for sale in sales)
        total_records = len(sales)
        unique_products = len(set(sale.product_name for sale in sales))
        unique_categories = len(set(sale.category for sale in sales))

        return {
            "total_revenue": total_revenue,
            "total_quantity_sold": total_quantity_sold,
            "total_records": total_records,
            "unique_products": unique_products,
            "unique_categories": unique_categories
        }

    finally:
        db.close()