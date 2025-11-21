import streamlit as st
import math

st.title("🔬 Scientific Calculator (Improved)")

# Angle mode: Degrees / Radians
angle_mode = st.radio("Angle Mode:", ["Radians", "Degrees"])

# User expression input
expression = st.text_input(
    "Enter expression (supports sin, cos, tan, log, sqrt, etc.):"
)

# Allowed functions (safe)
allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

# Wrap trigonometric functions to support degrees
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

# Include both radian & degree versions
if angle_mode == "Degrees":
    allowed.update({
        "sin": sin_deg,
        "cos": cos_deg,
        "tan": tan_deg
    })
else:
    # default radian mode uses math.sin, math.cos, math.tan
    pass

# Allow common built-ins
allowed.update({
    "abs": abs,
    "round": round
})

def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": {}}, allowed)
    except Exception as e:
        return f"Error: {e}"

if st.button("Calculate"):
    if expression.strip():
        result = safe_eval(expression)
        st.success(f"Result: {result}")
    else:
        st.warning("Please enter an expression.")

st.markdown("""
### 📘 Try examples:
#### ➤ Radians Mode:
- `sin(1)`
- `cos(0)`
- `tan(0.5)`
- `log(10)`
- `sqrt(144)`
- `2**10`

#### ➤ Degrees Mode:
- `sin(30)`
- `cos(60)`
- `tan(45)`
""")
