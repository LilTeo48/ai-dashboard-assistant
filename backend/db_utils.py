from backend.db import SessionLocal
from backend.models import Sale
import pandas as pd


def save_sales_to_db(df):
    db = SessionLocal()

    try:
        saved_count = 0
        skipped_count = 0

        for _, row in df.iterrows():
            existing_sale = db.query(Sale).filter(
                Sale.product_name == row["product_name"],
                Sale.category == row["category"],
                Sale.quantity_sold == int(row["quantity_sold"]),
                Sale.revenue == float(row["revenue"]),
                Sale.sale_date == row["sale_date"].date()
            ).first()

            if existing_sale:
                skipped_count += 1
                continue

            sale = Sale(
                product_name=row["product_name"],
                category=row["category"],
                quantity_sold=int(row["quantity_sold"]),
                revenue=float(row["revenue"]),
                sale_date=row["sale_date"].date()
            )

            db.add(sale)
            saved_count += 1

        db.commit()

        return saved_count, skipped_count

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()


def load_sales_from_db():
    db = SessionLocal()

    try:
        sales = db.query(Sale).all()

        data = [
            {
                "product_name": sale.product_name,
                "category": sale.category,
                "quantity_sold": sale.quantity_sold,
                "revenue": sale.revenue,
                "sale_date": sale.sale_date
            }
            for sale in sales
        ]

        return pd.DataFrame(data)

    finally:
        db.close()