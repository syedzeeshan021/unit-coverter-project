import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("Unit Converter")

# Sidebar: Select Conversion Category
conversion_category = st.sidebar.selectbox("Select Conversion Category", 
                                             ["Length", "Mass", "Temperature"])

# Conversion functions for each category
def convert_length(value, from_unit, to_unit):
    # Define conversion factors relative to meter
    factors = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    value_in_meters = value * factors[from_unit]
    return value_in_meters / factors[to_unit]

def convert_mass(value, from_unit, to_unit):
    # Define conversion factors relative to kilogram
    factors = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    value_in_kg = value * factors[from_unit]
    return value_in_kg / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Convert from input to Celsius first, then to target
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15

    # Convert Celsius to target unit
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

# Define unit options based on category
if conversion_category == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
elif conversion_category == "Mass":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
elif conversion_category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]

# User input: value, source unit, target unit
value = st.number_input("Enter value to convert", value=1.0)
from_unit = st.selectbox("From", units, key="from_unit")
to_unit = st.selectbox("To", units, key="to_unit")

# Convert based on the category selected
if conversion_category == "Length":
    result = convert_length(value, from_unit, to_unit)
elif conversion_category == "Mass":
    result = convert_mass(value, from_unit, to_unit)
elif conversion_category == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)

# Display the conversion result
st.markdown(f"### {value} {from_unit} = {result:.4f} {to_unit}")


# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Syed Zeeshan Iqbal")
