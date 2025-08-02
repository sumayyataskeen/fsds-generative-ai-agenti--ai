import streamlit as st
import math
import numpy as np

def main():
    st.set_page_config(
        page_title="Calculator App",
        page_icon="🧮",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .calculator-container {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .result-display {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-size: 1.5rem;
        text-align: right;
        margin-bottom: 1rem;
    }
    .button-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.5rem;
    }
    .calc-button {
        padding: 1rem;
        font-size: 1.2rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .calc-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .number-btn {
        background-color: #ffffff;
        color: #333333;
    }
    .operator-btn {
        background-color: #ff9500;
        color: white;
    }
    .function-btn {
        background-color: #007aff;
        color: white;
    }
    .clear-btn {
        background-color: #ff3b30;
        color: white;
    }
    .equals-btn {
        background-color: #34c759;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🧮 Calculator App</h1>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'display' not in st.session_state:
        st.session_state.display = "0"
    if 'previous_number' not in st.session_state:
        st.session_state.previous_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'new_number' not in st.session_state:
        st.session_state.new_number = True
    
    # Create two columns for calculator and scientific functions
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
        
        # Display
        st.markdown(f'<div class="result-display">{st.session_state.display}</div>', unsafe_allow_html=True)
        
        # Calculator buttons
        button_cols = st.columns(4)
        
        # Row 1: Clear, ±, %, ÷
        with button_cols[0]:
            if st.button("C", key="clear", use_container_width=True):
                st.session_state.display = "0"
                st.session_state.previous_number = None
                st.session_state.operation = None
                st.session_state.new_number = True
                st.rerun()
        
        with button_cols[1]:
            if st.button("±", key="plus_minus", use_container_width=True):
                if st.session_state.display != "0":
                    if st.session_state.display.startswith("-"):
                        st.session_state.display = st.session_state.display[1:]
                    else:
                        st.session_state.display = "-" + st.session_state.display
                st.rerun()
        
        with button_cols[2]:
            if st.button("%", key="percent", use_container_width=True):
                try:
                    value = float(st.session_state.display)
                    st.session_state.display = str(value / 100)
                except:
                    st.session_state.display = "Error"
                st.rerun()
        
        with button_cols[3]:
            if st.button("÷", key="divide", use_container_width=True):
                st.session_state.previous_number = float(st.session_state.display)
                st.session_state.operation = "÷"
                st.session_state.new_number = True
                st.rerun()
        
        # Row 2: 7, 8, 9, ×
        with button_cols[0]:
            if st.button("7", key="7", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "7"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "7"
                st.rerun()
        
        with button_cols[1]:
            if st.button("8", key="8", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "8"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "8"
                st.rerun()
        
        with button_cols[2]:
            if st.button("9", key="9", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "9"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "9"
                st.rerun()
        
        with button_cols[3]:
            if st.button("×", key="multiply", use_container_width=True):
                st.session_state.previous_number = float(st.session_state.display)
                st.session_state.operation = "×"
                st.session_state.new_number = True
                st.rerun()
        
        # Row 3: 4, 5, 6, -
        with button_cols[0]:
            if st.button("4", key="4", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "4"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "4"
                st.rerun()
        
        with button_cols[1]:
            if st.button("5", key="5", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "5"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "5"
                st.rerun()
        
        with button_cols[2]:
            if st.button("6", key="6", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "6"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "6"
                st.rerun()
        
        with button_cols[3]:
            if st.button("-", key="minus", use_container_width=True):
                st.session_state.previous_number = float(st.session_state.display)
                st.session_state.operation = "-"
                st.session_state.new_number = True
                st.rerun()
        
        # Row 4: 1, 2, 3, +
        with button_cols[0]:
            if st.button("1", key="1", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "1"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "1"
                st.rerun()
        
        with button_cols[1]:
            if st.button("2", key="2", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "2"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "2"
                st.rerun()
        
        with button_cols[2]:
            if st.button("3", key="3", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "3"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "3"
                st.rerun()
        
        with button_cols[3]:
            if st.button("+", key="plus", use_container_width=True):
                st.session_state.previous_number = float(st.session_state.display)
                st.session_state.operation = "+"
                st.session_state.new_number = True
                st.rerun()
        
        # Row 5: 0, ., =
        zero_cols = st.columns([2, 1, 1])
        
        with zero_cols[0]:
            if st.button("0", key="0", use_container_width=True):
                if st.session_state.new_number:
                    st.session_state.display = "0"
                    st.session_state.new_number = False
                else:
                    st.session_state.display += "0"
                st.rerun()
        
        with zero_cols[1]:
            if st.button(".", key="decimal", use_container_width=True):
                if "." not in st.session_state.display:
                    st.session_state.display += "."
                st.rerun()
        
        with zero_cols[2]:
            if st.button("=", key="equals", use_container_width=True):
                if st.session_state.previous_number is not None and st.session_state.operation:
                    current = float(st.session_state.display)
                    previous = st.session_state.previous_number
                    
                    if st.session_state.operation == "+":
                        result = previous + current
                    elif st.session_state.operation == "-":
                        result = previous - current
                    elif st.session_state.operation == "×":
                        result = previous * current
                    elif st.session_state.operation == "÷":
                        if current != 0:
                            result = previous / current
                        else:
                            result = "Error"
                    
                    st.session_state.display = str(result)
                    st.session_state.previous_number = None
                    st.session_state.operation = None
                    st.session_state.new_number = True
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🔬 Scientific Functions")
        
        # Scientific calculator functions
        st.markdown("#### Basic Functions")
        
        if st.button("√", key="sqrt", use_container_width=True):
            try:
                value = float(st.session_state.display)
                if value >= 0:
                    st.session_state.display = str(math.sqrt(value))
                else:
                    st.session_state.display = "Error"
            except:
                st.session_state.display = "Error"
            st.rerun()
        
        if st.button("x²", key="square", use_container_width=True):
            try:
                value = float(st.session_state.display)
                st.session_state.display = str(value ** 2)
            except:
                st.session_state.display = "Error"
            st.rerun()
        
        if st.button("1/x", key="reciprocal", use_container_width=True):
            try:
                value = float(st.session_state.display)
                if value != 0:
                    st.session_state.display = str(1 / value)
                else:
                    st.session_state.display = "Error"
            except:
                st.session_state.display = "Error"
            st.rerun()
        
        st.markdown("#### Trigonometric Functions")
        
        trig_cols = st.columns(2)
        
        with trig_cols[0]:
            if st.button("sin", key="sin", use_container_width=True):
                try:
                    value = float(st.session_state.display)
                    st.session_state.display = str(math.sin(math.radians(value)))
                except:
                    st.session_state.display = "Error"
                st.rerun()
            
            if st.button("cos", key="cos", use_container_width=True):
                try:
                    value = float(st.session_state.display)
                    st.session_state.display = str(math.cos(math.radians(value)))
                except:
                    st.session_state.display = "Error"
                st.rerun()
        
        with trig_cols[1]:
            if st.button("tan", key="tan", use_container_width=True):
                try:
                    value = float(st.session_state.display)
                    st.session_state.display = str(math.tan(math.radians(value)))
                except:
                    st.session_state.display = "Error"
                st.rerun()
            
            if st.button("log", key="log", use_container_width=True):
                try:
                    value = float(st.session_state.display)
                    if value > 0:
                        st.session_state.display = str(math.log10(value))
                    else:
                        st.session_state.display = "Error"
                except:
                    st.session_state.display = "Error"
                st.rerun()
        
        st.markdown("#### Constants")
        
        const_cols = st.columns(2)
        
        with const_cols[0]:
            if st.button("π", key="pi", use_container_width=True):
                st.session_state.display = str(math.pi)
                st.rerun()
            
            if st.button("e", key="e", use_container_width=True):
                st.session_state.display = str(math.e)
                st.rerun()
        
        with const_cols[1]:
            if st.button("Rand", key="random", use_container_width=True):
                st.session_state.display = str(np.random.random())
                st.rerun()
            
            if st.button("Factorial", key="factorial", use_container_width=True):
                try:
                    value = int(float(st.session_state.display))
                    if value >= 0:
                        st.session_state.display = str(math.factorial(value))
                    else:
                        st.session_state.display = "Error"
                except:
                    st.session_state.display = "Error"
                st.rerun()
    
    # History section
    st.markdown("---")
    st.markdown("### 📊 Calculation History")
    
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    # Add current calculation to history
    if st.session_state.previous_number is not None and st.session_state.operation:
        history_entry = f"{st.session_state.previous_number} {st.session_state.operation} {st.session_state.display}"
        if history_entry not in st.session_state.history:
            st.session_state.history.append(history_entry)
    
    # Display history
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-10:])):  # Show last 10 entries
            st.text(f"{len(st.session_state.history) - i}: {entry}")
    else:
        st.text("No calculations yet")
    
    # Clear history button
    if st.button("Clear History", key="clear_history"):
        st.session_state.history = []
        st.rerun()

if __name__ == "__main__":
    main() 