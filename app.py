# ============================================
# 🧮 Streamlit Scientific Calculator App
# ============================================

import streamlit as st
import math

# Page setup
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Scientific Calculator")
st.write("Perform arithmetic and scientific calculations easily!")

# Input section
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number:", value=0.0)
with col2:
    num2 = st.number_input("Enter second number (if needed):", value=0.0)

# Operation selector
operation = st.selectbox(
    "Choose operation:",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Power (xʸ)",
        "Square Root (√x)",
        "Logarithm (log₁₀x)",
        "Natural Logarithm (ln x)",
        "Sine (sin x)",
        "Cosine (cos x)",
        "Tangent (tan x)",
        "Factorial (x!)",
        "Absolute Value (|x|)"
    ]
)

# Calculate button
if st.button("Calculate"):
    try:
        result = None
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
        elif operation == "Power (xʸ)":
            result = math.pow(num1, num2)
        elif operation == "Square Root (√x)":
            if num1 < 0:
                st.error("❌ Error: Cannot take square root of a negative number.")
            else:
                result = math.sqrt(num1)
        elif operation == "Logarithm (log₁₀x)":
            if num1 <= 0:
                st.error("❌ Error: Logarithm undefined for non-positive numbers.")
            else:
                result = math.log10(num1)
        elif operation == "Natural Logarithm (ln x)":
            if num1 <= 0:
                st.error("❌ Error: Natural log undefined for non-positive numbers.")
            else:
                result = math.log(num1)
        elif operation == "Sine (sin x)":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine (cos x)":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent (tan x)":
            result = math.tan(math.radians(num1))
        elif operation == "Factorial (x!)":
            if num1 < 0 or not float(num1).is_integer():
                st.error("❌ Error: Factorial only defined for non-negative integers.")
            else:
                result = math.factorial(int(num1))
        elif operation == "Absolute Value (|x|)":
            result = abs(num1)

        # Display result
        if result is not None:
            st.success(f"✅ Result: {result}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Supports standard and scientific operations")
