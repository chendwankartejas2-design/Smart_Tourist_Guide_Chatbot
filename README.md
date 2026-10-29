# 🌍 Smart Tourist Guide & AI Trip Planner

An AI-powered travel assistant designed to help users explore destinations, get travel-related information, and plan trips more conveniently. The project integrates a conversational AI chatbot with a web-based interface to provide an interactive travel-planning experience.

## 📌 Project Overview

The **Smart Tourist Guide & AI Trip Planner** aims to simplify travel planning by providing users with an intelligent assistant that can answer travel-related queries and help them discover destinations. By integrating AI capabilities with a web application, the system offers a convenient way to explore travel options and plan journeys.

## ✨ Features

- 🤖 **AI-Powered Chatbot:** Interact with an intelligent assistant for travel-related queries.
- 🗺️ **Travel Assistance:** Get information and suggestions to support trip planning.
- 🧳 **Trip Planning:** Get assistance in organizing travel plans and itineraries.
- 🎙️ **Voice Assistant:** Voice-based interaction for a more convenient user experience.
- 💬 **Interactive Interface:** User-friendly web interface for communicating with the AI assistant.
- ⚡ **AI Integration:** Uses the Google Gemini API to generate conversational responses.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend:** Flask / FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **AI Integration:** Google Gemini API
- **Database:** SQLite (depending on the project version)

## 🏗️ Project Structure

```text
Smart-Tourist-Guide/
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*Note: The structure above is illustrative. Update it to match your actual project files.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Smart-Tourist-Guide
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Keep your API key private. Never upload your actual API key to GitHub.

### 5. Run the Application

Use the command that matches your project's backend.

For Flask:

```bash
python app.py
```

For FastAPI, if your application instance is named `app` inside `app.py`:

```bash
uvicorn app:app --reload
```

Open the local URL displayed in your terminal to access the application.

## 🔐 Security

- Store API keys in environment variables.
- Add `.env` and virtual environment folders to `.gitignore`.
- Never commit passwords, API keys, or other sensitive credentials.

## 🎯 Project Objectives

- Make travel information more accessible through conversational AI.
- Simplify the process of exploring destinations and planning trips.
- Demonstrate the practical application of AI integration in web development.
- Build an interactive and user-friendly travel assistance
