import streamlit as st

# Unit Conversion Functionality
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# Streamlit App
st.title("Unit Converter App")

conversion_type = st.selectbox("Select Conversion Type:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")