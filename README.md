# College-Chatbot

# 🎓 Brainware University AI Chatbot

An intelligent, AI-powered chatbot for Brainware University that answers student queries about admissions, courses, fees, placement, hostel, and more — served via a Python Flask backend with a sleek glassmorphism frontend.

---

## 📁 Project Structure

```
brainware-chatbot/
├── app.py               # Flask backend — handles /chat API endpoint
├── templates/
│   └── index.html       # Frontend UI (glassmorphism chat interface)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ✨ Features

- 🤖 AI-powered responses via a `/chat` REST API
- 💬 Real-time chat UI with typing animation
- 🎨 Glassmorphism dark-themed design with animated background
- ⚡ Quick-access chips: Admission, Fees, Courses, Placement, Hostel, Contact, Rankings, Research
- 📊 Live stats bar (Placement rate, Programs, Recruiters, Students, WB Ranking)
- 📱 Responsive layout, keyboard-friendly (Enter to send)

---

## 🛠️ Tech Stack

| Layer     | Technology                  |
|-----------|-----------------------------|
| Frontend  | HTML5, CSS3, Vanilla JS     |
| Backend   | Python 3, Flask             |
| AI/NLP    | (your model/API here)       |
| Styling   | Custom CSS, Glassmorphism   |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com//brainware-chatbot.git
cd brainware-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

The server starts at `http://127.0.0.1:5000/`

Open your browser and visit: **http://127.0.0.1:5000/**

---

## 🔌 API Reference

### `POST /chat`

Accepts a user message and returns the bot's reply.

**Request:**
```json
{
  "message": "What are the available courses?"
}
```

**Response:**
```json
{
  "reply": "Brainware University offers 70+ programs including B.Tech, MBA, BCA, MCA..."
}
```

---

