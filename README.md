# AI Dashboard Assistant

AI-powered analytics dashboard built with Python, Streamlit, FastAPI, and OpenAI APIs that generates business insights from sales datasets using natural language prompts.

---

## Features

* AI-generated business insights
* Interactive analytics dashboard
* Revenue visualization charts
* Dynamic KPI metrics
* Natural language business questions
* OpenAI API integration
* CSV upload support
* Dashboard filtering system
* AI chat history
* Streamlit frontend
* FastAPI backend architecture
* Secure environment variable handling

---

## Tech Stack

### Backend

* Python
* FastAPI
* OpenAI API
* SQLAlchemy

### Frontend

* Streamlit

### Data & Analytics

* Pandas
* CSV datasets
* Data visualization

---

## Project Structure

```text
ai-dashboard-assistant/
│
├── backend/
│   ├── ai_service.py
│   ├── db.py
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── sample_sales.csv
│
├── database/
│   └── schema.sql
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Features Overview

### AI-Powered Analytics

Ask natural language business questions such as:

* Which product generated the most revenue?
* What category performs best?
* Which products should be promoted more?
* What business insight can you identify?

The OpenAI integration analyzes filtered datasets and generates concise business insights.

---

### Dashboard Filters

Users can dynamically filter data by:

* Product category
* Product name
* Sale date range

Charts, KPIs, tables, and AI responses update automatically based on selected filters.

---

### CSV Upload Support

Users can upload custom CSV datasets directly into the dashboard.

Required columns:

```text
product_name
category
quantity_sold
revenue
sale_date
```

---

### AI Chat History

The dashboard stores previous user prompts and AI-generated insights during the session to create a conversational analytics experience.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LilTeo48/ai-dashboard-assistant.git
cd ai-dashboard-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

Start Streamlit:

```bash
streamlit run dashboard/app.py
```

Start FastAPI backend:

```bash
uvicorn backend.main:app --reload
```

---

## Example AI Insight

> Electronics is the strongest category, generating the highest total revenue, led by the Monitor product despite lower sales volume.

---

## Future Improvements

* PostgreSQL integration
* Docker deployment
* Cloud hosting
* Authentication system
* Multi-user support
* Natural language to SQL conversion

---

## Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48

