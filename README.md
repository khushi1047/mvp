# 🐰 Talking Rabbitt – AI Data Chatbot

Talking Rabbitt is a simple **AI-powered data assistant** that allows users to **talk to their business data using natural language**.

Users can upload a CSV dataset and ask questions like:

* Which region has the highest revenue?
* Show revenue trend over time
* Which product generated the most revenue?

The system analyzes the dataset and returns **clear answers along with visualizations**.

---

## Features

* Conversational queries on business data
* CSV dataset upload
* Automatic chart generation
* Built-in sample dataset for quick testing

---

## Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* OpenAI API

---

## Project Structure

```
talking-rabbitt/
│
├── app.py
├── sample_sales.csv
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run the App

```
streamlit run app.py
```

The app will open in your browser.

---

## Example Questions

* Which region has the highest revenue?
* Show revenue trend
* Which product generates most revenue?

---

This project demonstrates the **core idea of Talking Rabbitt: turning business analytics into a simple conversation.**
