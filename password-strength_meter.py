import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #639DE4;
        }
        .title, .subheader, .stSubheader {
            text-align: center;
            font-size: 2em;
            color: white !important;
        }
        .convert-btn {
            background-color: #AC1754 !important;
            color: white !important;
            font-size: 1.2em !important;
            padding: 10px 20px !important;
        }
        .result-box {
            font-size: 1.5em;
            font-weight: bold;
            color: #AC1754;
            text-align: center;
        }
        .weak-password {
            color: red !important;
            font-size: 1.5em;
            text-align: center;
        }
        .strong-password {
            color: green !important;
            font-size: 1.5em;
            text-align: center;
        }
        .header-text {
            font-size: 1.5em;
            text-align: center;
            color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<h1 class="title">Password Strength Checker</h1>', unsafe_allow_html=True)

# Function to check password strength
# Function to check password strength
def check_Password(password):
    if password:
        if len(password) < 8:
            st.markdown('<h2 class="weak-password">Weak Password! Password must be at least 8 characters long!</h2>', unsafe_allow_html=True)
            return
        if not any(char.isdigit() for char in password):
            st.markdown('<h2 class="weak-password">Weak Password! Password must contain at least 1 digit</h2>', unsafe_allow_html=True)
            return
        if not any(char.isupper() for char in password):
            st.markdown('<h2 class="weak-password">Weak Password! Password must contain at least 1 uppercase letter</h2>', unsafe_allow_html=True)
            return
        if not any(char.islower() for char in password):
            st.markdown('<h2 class="weak-password">Weak Password! Password must contain at least 1 lowercase letter</h2>', unsafe_allow_html=True)
            return
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",<>\./?\\|`~]', password):  # Updated regex pattern
            st.markdown('<h2 class="weak-password">Weak Password! Password must contain at least 1 special character</h2>', unsafe_allow_html=True)
            return
        st.markdown('<h2 class="strong-password">Strong Password!</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 class="header-text">Please enter a password</h2>', unsafe_allow_html=True)


# Create password input box
st.markdown('<div class="input-container">', unsafe_allow_html=True)
password = st.text_input("Enter a Password", key="password", type="password")
st.markdown('</div>', unsafe_allow_html=True)

# Check password strength
check_Password(password)
