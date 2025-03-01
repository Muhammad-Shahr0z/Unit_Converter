import streamlit as st


#  Global conversion factors...
# Nested Dictionary..
conversion_factors = {
    "Length": {
        "meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000, "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701
    },
    "Weight": {
        "kilogram": 1, "gram": 1000, "milligram": 1e6, "pound": 2.20462, "ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
    },
    "Volume": {
        "liter": 1, "milliliter": 1000, "gallon": 0.264172, "quart": 1.05669, "pint": 2.11338, "cup": 4.22675, "fluid ounce": 33.814
    },
    "Speed": {
        "meter per second": 1, "kilometer per hour": 3.6, "mile per hour": 2.23694, "knot": 1.94384
    },
    "Time": {
        "second": 1, "minute": 1/60, "hour": 1/3600, "day": 1/86400
    },
    "Area": {
        "square meter": 1, "square kilometer": 1e-6, "square mile": 3.861e-7, "square yard": 1.19599, "square foot": 10.7639, "acre": 0.000247105
    },
    "Data Storage": {
        "byte": 1, "kilobyte": 1/1024, "megabyte": 1/(1024**2), "gigabyte": 1/(1024**3), "terabyte": 1/(1024**4)
    }
}

# function TO conversion_factors...
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
    
    return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])


#HEADINGS....
st.set_page_config(page_title="Unit Converter by Shahroz", layout="wide")
st.title(" Unit Converter")
st.write("Convert between different units easily!")

# Saare available categories list me rakh liyee hain...
categories = list(conversion_factors.keys()) 

#CATEGORY CHECKBOX....
category = st.selectbox("Select Category", categories)

if category:
    units = list(conversion_factors[category].keys())
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value:.4f} {from_unit} = {result:.4f} {to_unit}")


# Custom CSS for Footer
footer_style = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        width: 100%;
        background-color: #f8f9fa;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        color: #333;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
"""
st.markdown(footer_style, unsafe_allow_html=True)

# Footer HTML
footer = """
    <div class="footer">
        Made with ❤️ by Muhammad Shahroz
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
