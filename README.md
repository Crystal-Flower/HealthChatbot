# 🩺 HealthBuddy AI - Gemini Powered Assistant

**HealthBuddy** is a lightweight, AI-powered health consultation chatbot built using Python, Streamlit, and Google's Gemini API. It serves as a compassionate first-point-of-contact for general health queries, symptom explanations, and wellness tips, while strictly adhering to safety protocols and emphasizing that it is **not** a replacement for a doctor.

---

## 🚀 Features

* **Conversational Interface:** Remembers previous messages for a natural chat flow.
* **Empathetic Persona:** System instructions ensure the AI responds with a calm, professional, and caring tone.
* **Medical Disclaimer:** Automatically appends safety warnings to advice.
* **Gemini 1.5 Flash:** Uses Google's efficient, low-latency model for quick responses.
* **Emergency Awareness:** (Logical instruction) Instructed to direct users to emergency services for critical keywords.

---

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Frontend:** Streamlit
* **LLM Provider:** Google Generative AI (Gemini API)

---

## 📋 Prerequisites

Before you begin, ensure you have:

1. Python installed on your machine.
2. A Google Cloud API Key (Get it from [Google AI Studio](https://aistudio.google.com/)).

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

(If you haven't created a git repo yet, just create a folder for your project).

### 2. Create a Virtual Environment (Recommended)

It is best practice to run this in an isolated environment.

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Create a `requirements.txt` file (see below) or install directly:

```bash
pip install streamlit google-generativeai

```

### 4. Configure API Key

Open `health_bot.py` and replace the placeholder with your key:

```python
API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

```

*(Note: For production apps, use environment variables or Streamlit secrets).*

---

## 🏃‍♂️ How to Run

Navigate to your project folder in the terminal and execute:

```bash
streamlit run main.py

```

A browser tab should automatically open at `http://localhost:8501`.

---

## 📂 Project Structure

```text
health-chatbot/
├── health_bot.py        # Main application code
├── requirements.txt     # List of python dependencies
└── README.md            # Documentation

```

---

## ⚠️ Important Medical Disclaimer

**This application is for educational and informational purposes only.**

* The AI is not a doctor and cannot provide a definitive medical diagnosis.
* It cannot prescribe medication.
* Users are strictly advised to consult a certified medical professional for any health concerns.
* **In case of emergency:** The user should immediately contact local emergency services (e.g., 911, 112).

---

## 🔮 Future Roadmap

* [ ] **Image Analysis:** Allow users to upload medical reports or skin images for analysis.
* [ ] **Voice Mode:** Add Speech-to-Text for hands-free consultation.
* [ ] **PDF Export:** Allow users to download a summary of the chat to show their doctor.

---

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
