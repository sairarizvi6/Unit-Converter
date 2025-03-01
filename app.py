import streamlit as st 

# Custom CSS for full dark theme and better styling
st.markdown("""
    <style>
    /* Dark Theme */
    body {
        background-color: #121212;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    .stReLeftbox, .stNumberInput, .stButton {
        border-radius: 8px;
    }
    /* Centered Gradient Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #8A2BE2, #6A0DAD);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6A0DAD, #8A2BE2);
    }
    /* Bold Labels */
    label {
        font-weight: bold;
        font-size: 22px
    }
    /* Result Styling */
    .result-text {
        font-weight: bold;
        color: #E0AFFF;
        font-size: 22px;
    }
    </style>
""", unsafe_allow_html=True)

# Function Definitions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Kilometers": 1.0,
        "Meters": 1000.0,
        "Miles": 0.621371,
        "Feet": 3280.84
    }
    value_in_km = value / length_units[from_unit]
    return value_in_km * length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value  

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 1000.0,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    value_in_kg = value / weight_units[from_unit]
    return value_in_kg * weight_units[to_unit]

# App Title
st.markdown("<h1 style='text-align: center; color: white;'>⚡ Unit Converter⚡ </h1>", unsafe_allow_html=True)

# Row Layout for Select Conversion Type & Value Input
col1, col2 = st.columns(2)
with col1:
    conversion_type = st.selectbox("**Select Conversion Type:**", ["Length", "Temperature", "Weight"])
with col2:
    value = st.number_input("**Enter the value:**", min_value=0.0, format="%.2f")

# Conversion UI
from_unit, to_unit = None, None

if conversion_type == "Length":
    from_unit = st.selectbox("**From:**", ["Kilometers", "Meters", "Miles", "Feet"])
    to_unit = st.selectbox("**To:**", ["Kilometers", "Meters", "Miles", "Feet"])

elif conversion_type == "Temperature":
    from_unit = st.selectbox("**From:**", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("**To:**", ["Celsius", "Fahrenheit"])

elif conversion_type == "Weight":
    from_unit = st.selectbox("**From:**", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("**To:**", ["Kilograms", "Grams", "Pounds", "Ounces"])

# Left-Aligned Convert Button
if st.button("Convert"):
    result = None
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)

    if result is not None:
        st.markdown(f'<p class="result-text">{value} {from_unit} = {result:.2f} {to_unit}</p>', 
                    unsafe_allow_html=True)