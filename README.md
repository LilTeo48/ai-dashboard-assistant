# AI Dashboard Assistant

An AI-powered business intelligence dashboard built with **Python, Streamlit, FastAPI, PostgreSQL, Docker, Plotly, and OpenAI**.

The application allows users to upload sales data, analyze key business metrics, visualize trends, and generate AI-powered insights through natural language questions.

---

## Live Demo

🔗 Streamlit Deployment: https://ai-dashboard-assistant-kvmbsrfuq29ako3schq24s.streamlit.app/


---

## Features

### Data Management

* Upload CSV sales datasets
* Validate uploaded data structure
* Download filtered datasets as CSV
* PostgreSQL integration for persistent storage

### Interactive Dashboard

* Revenue KPI metrics
* Quantity sold tracking
* Average revenue calculations
* Product and category filters
* Date range filtering

### Data Visualization

* Revenue by Product charts
* Revenue by Category charts
* Interactive Plotly visualizations
* Dark-mode dashboard design

### AI-Powered Insights

* Ask questions about your sales data
* OpenAI-powered business analysis
* Natural language querying
* Context-aware responses based on filtered datasets

### Backend Services

* FastAPI REST API
* PostgreSQL database integration
* SQLAlchemy ORM
* Dockerized deployment environment

---

## Tech Stack

### Frontend

* Streamlit
* Plotly

### Backend

* Python
* FastAPI
* SQLAlchemy

### Database

* PostgreSQL

### AI Integration

* OpenAI API

### Deployment & DevOps

* Docker
* Docker Compose
* GitHub
* Streamlit Cloud

---

## Project Architecture

```text
Streamlit Dashboard
        │
        ▼
FastAPI Backend
        │
        ▼
PostgreSQL Database
        │
        ▼
OpenAI API
```

---

## Local Installation

### Clone Repository

```bash
git clone https://github.com/LilTeo48/ai-dashboard-assistant.git
cd ai-dashboard-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_dashboard_db
```

### Run with Docker

```bash
docker compose up --build
```

### Run Streamlit

```bash
streamlit run dashboard/app.py
```

---

## API Endpoints

### Sales Data

```http
GET /sales
```

Returns all sales records.

### Top Products

```http
GET /sales/top-products
```

Returns products ranked by revenue.

### Sales Summary

```http
GET /sales/summary
```

Returns dashboard KPI metrics.

---

## Screenshots

### Dashboard Overview

Add dashboard screenshot here.

### Revenue Analytics

Add chart screenshot here.

### AI Insights

Add AI assistant screenshot here.

---

## Future Enhancements

* User authentication
* Hosted PostgreSQL database
* Production FastAPI deployment
* Advanced analytics
* Forecasting and trend analysis
* Export to PDF reports
* Role-based access control

---

## Author

**Tyler Chadwick**

* GitHub: https://github.com/LilTeo48
* LinkedIn: Add LinkedIn URL

---

## License

MIT License



Author
Tyler Chadwick

GitHub: https://github.com/LilTeo48
