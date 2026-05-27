# AI Dashboard Assistant

AI-powered analytics dashboard built with Python, Streamlit, FastAPI, and OpenAI APIs that generates business insights from sales datasets using natural language prompts.

---

## Features

- AI-generated business insights
- Interactive analytics dashboard
- Revenue visualization charts
- Natural language business questions
- OpenAI API integration
- Streamlit frontend
- FastAPI backend architecture
- Secure environment variable handling

---

## Tech Stack

### Backend
- Python
- FastAPI
- OpenAI API
- SQLAlchemy

### Frontend
- Streamlit

### Data & Analytics
- Pandas
- CSV datasets
- Data visualization

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
Installation

Clone the repository:

git clone https://github.com/LilTeo48/ai-dashboard-assistant.git
cd ai-dashboard-assistant

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here
Run the Application

Start Streamlit:

streamlit run dashboard/app.py

Start FastAPI backend:

uvicorn backend.main:app --reload
Example Questions
Which product generated the most revenue?
What category performed best?
Which products sold the least?
What business insights can you identify?
What inventory should be promoted more?
Example AI Insight

Electronics is the strongest category, generating the highest total revenue, led by the Monitor product despite lower sales volume.

Future Improvements
CSV file uploads
Natural language to SQL conversion
PostgreSQL integration
Authentication system
Dashboard filters
Multi-user support
Docker deployment
Cloud hosting
Author

Tyler Chadwick

GitHub:
https://github.com/LilTeo48
