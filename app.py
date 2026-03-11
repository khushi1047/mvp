import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# configure gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Talking Rabbitt", layout="wide")

st.title("🐰 Talking Rabbitt")
st.subheader("Talk to your business data")

st.write("Upload a CSV or use the sample dataset.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("sample_sales.csv")
    st.info("Using internal sample dataset")

st.write("### Data Preview")
st.dataframe(df)

question = st.text_input("Ask a business question")

if question:

    prompt = f"""
You are a data analyst.

Dataset columns:
{list(df.columns)}

User question:
{question}

Write pandas code to answer the question.

Rules:
- dataframe name is df
- return only python code
"""

    response = model.generate_content(prompt)

    code = response.text.replace("```python", "").replace("```", "").strip()

    st.write("### Generated Code")
    st.code(code)

    try:
        result = eval(code)

        st.write("### Result")
        st.write(result)

        # optional visualization
        if isinstance(result, pd.Series):

            st.write("### Visualization")

            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)

            st.pyplot(fig)

    except Exception as e:
        st.error("Error running generated code")
        st.write(e)