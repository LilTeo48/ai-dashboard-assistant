# AI Dashboard Assistant

AI-powered analytics dashboard built with Python, Streamlit, FastAPI, and OpenAI APIs that generates business insights from sales datasets using natural language prompts.

---

## Features

### AI-Powered Data Analysis

* Ask natural language questions about sales data using OpenAI.
* Generate business insights directly from uploaded datasets.
* Maintain AI chat history throughout the session.

### Interactive Dashboard

* Upload custom CSV files for analysis.
* Filter data by category, product, and date range.
* View key business metrics including revenue and quantity sold.
* Visualize revenue by product and category.

### Database Integration

* Save sales data to PostgreSQL.
* Load sales data directly from PostgreSQL.
* Prevent duplicate records from being inserted.
* Export filtered datasets as CSV files.

### FastAPI Backend

* REST API built with FastAPI.
* Interactive Swagger/OpenAPI documentation.
* Sales analytics endpoints:

  * `/sales`
  * `/sales/top-products`
  * `/sales/categories`
  * `/sales/summary`

### Data Processing

* SQLAlchemy ORM integration.
* PostgreSQL relational database storage.
* CSV ingestion and validation.
* Data filtering and transformation workflows.


## Architecture

```text
Streamlit Dashboard
        │
        ▼
     FastAPI
        │
        ▼
   SQLAlchemy
        │
        ▼
    PostgreSQL
```

### Backend Components

* **Streamlit**: User interface, charts, filters, AI interactions.
* **FastAPI**: REST API layer for sales analytics.
* **SQLAlchemy**: ORM for database communication.
* **PostgreSQL**: Persistent data storage.
* **OpenAI API**: AI-powered business insights.


## Future Improvements

* Dockerize the application stack.
* Deploy FastAPI backend to the cloud.
* Connect Streamlit directly to FastAPI endpoints.
* Add authentication and user accounts.
* Implement advanced analytics and forecasting.
* Add Plotly visualizations and dashboard pages.
* Create automated ETL workflows.
* Build a React frontend client.


Author
Tyler Chadwick

GitHub: https://github.com/LilTeo48
