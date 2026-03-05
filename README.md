                                                    
# 💰 Personal Expenses Tracker

A clean, full-stack **Personal Expenses Tracker** web application built with **Python**, **SQLite**, **Tailwind CSS**, and **HTML**. Track your daily spending, categorize expenses, and stay on top of your finances — all from your browser.

---

## 🖥️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3  |
| Database | SQLite · SQLAlchemy ORM |
| Frontend | HTML · Tailwind CSS (CDN) · Vanilla JS |
| Templating | Jinja2 |
| Server | Uvicorn (ASGI) |

---

## ✨ Features

- ➕ **Add expenses** with title, amount, category, date, and description
- 🗑️ **Delete expenses** instantly
- 💵 **Live total** — running sum updates automatically
- 🏷️ **Categories** — Food, Transport, Shopping, Bills, Health, Other
- 📱 **Responsive UI** — works on desktop and mobile
- 🗃️ **Persistent storage** — data saved in a local SQLite database
- ⚡ **REST API** — clean JSON endpoints ready for extension

---

## 📁 Project Structure

```
expenses-tracker/
├── main.py               # FastAPI app entry point
├── database.py           # SQLite connection & session
├── models.py             # SQLAlchemy ORM model
├── schemas.py            # Pydantic request/response schemas
├── routers/
│   └── expenses.py       # API routes (GET, POST, DELETE)
├── static/               # Static assets (CSS/JS files)
├── templates/
│   └── index.html        # Frontend — HTML + Tailwind CSS
├── expenses.db           # Auto-generated SQLite database
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- VS Code (recommended) or any code editor

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/expenses-tracker.git
cd expenses-tracker
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

### 5. Open in Browser

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/expenses/` | Fetch all expenses |
| `POST` | `/expenses/` | Add a new expense |
| `DELETE` | `/expenses/{id}` | Delete an expense by ID |

### Example Request — Add Expense

```bash
curl -X POST "http://127.0.0.1:8000/expenses/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Lunch",
    "amount": 150.00,
    "category": "Food",
    "date": "2025-03-06",
    "description": "Rice and curry"
  }'
```

### Example Response

```json
{
  "id": 1,
  "title": "Lunch",
  "amount": 150.0,
  "category": "Food",
  "date": "2025-03-06",
  "description": "Rice and curry"
}
```

> 📖 Interactive API docs available at: `http://127.0.0.1:8000/docs`

---

## 📦 requirements.txt

```
fastapi
uvicorn
sqlalchemy
jinja2
python-multipart
```

Generate it with:
```bash
pip freeze > requirements.txt
```

---

## 🗺️ Roadmap

- [ ] Edit / update existing expenses
- [ ] Filter by category or date range
- [ ] Monthly spending summary
- [ ] Pie/bar chart visualization (Chart.js)
- [ ] Export expenses to CSV
- [ ] User authentication (login / register)
- [ ] Dark mode toggle

---


## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Abu Talha**

---

> Built with ❤️ using -- Python 
