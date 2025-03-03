import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #f8f9fa;
        }
        .title {
            text-align: center;
            font-size: 2em;
            color: #007bff;
        }
        .convert-btn {
            background-color: #28a745 !important;
            color: white !important;
            font-size: 1.2em !important;
            padding: 10px 20px !important;
        }
        .result-box {
            font-size: 1.5em;
            font-weight: bold;
            color: #28a745;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subheader
st.title("🔄 Unit Converter")
st.subheader("Easily convert between different units!")
