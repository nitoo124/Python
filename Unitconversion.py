import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: pink;
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
    </style>
""", unsafe_allow_html=True)

# Title and subheader
st.markdown("<h1 class='title'>🔄 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>Easily convert between different units!</h2>", unsafe_allow_html=True)

# Conversion Functions
def Convert_Length (value, unit_from, unit_to):
        length_units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
        return value * length_units[unit_from] / length_units[unit_to]

def Convert_weight(value, unit_from, unit_to):
            weight_units = {"Grams": 1, "Kilograms": 1000, "Pounds": 453.592, "Ounces": 28.3495}
            return value * weight_units[unit_from] / weight_units[unit_to]

def Convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return value
    elif unit_from == "Celsius" and unit_to == "Fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "Celsius" and unit_to == "Kelvin":
        return value + 273.15
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 5/9
    elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif unit_from == "Kelvin" and unit_to == "Celsius":
        return value - 273.15
    elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    
    # Conversion type selection
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
     st.subheader("Length Conversion")
     value =st.number_input("Enter value")
     unit_from = st.selectbox('From', ["Meters","Kilometers", "Miles", "Feet"])
     unit_to = st.selectbox('To', ["Meters","Kilometers", "Miles", "Feet"])
     if st.button("Convert", key="lenght_btn" ):
       result = Convert_Length(value,unit_from, unit_to)
       st.success(f"Converted value: {result:.2f} {unit_to}")

elif conversion_type == "Weight":
     st.subheader("Weight Conversion")
     value = st.number_input("Enter value")
     unit_from = st.selectbox("From", ["Grams", "Kilograms", "Pounds", "Ounces"])
     unit_to = st.selectbox("To", ["Grams", "Kilograms", "Pounds", "Ounces"])
     if st.button("Convert", key="weight_btn"):
          result = Convert_weight(value, unit_from, unit_to)
          st.success(f"Converted value: {result: .2f} {unit_to}")

elif conversion_type == "Temperature":
     st.subheader("Temperature Conversion")
     value = st.number_input("Enter value")
     unit_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
     unit_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
     if st.button("Convert", key="Temperature_btn"):
          result = Convert_temperature(value, unit_from, unit_to)
          st.success(f"Converted value: {result: .2f} {unit_to}")