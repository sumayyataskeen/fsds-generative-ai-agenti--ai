import streamlit as st
import random
from datetime import datetime

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Predefined responses for the chatbot
RESPONSES = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you!",
        "Hello! I'm your friendly chatbot assistant."
    ],
    "how are you": [
        "I'm doing great, thanks for asking! How about you?",
        "I'm functioning perfectly! How are you?",
        "All systems operational! How are you doing?"
    ],
    "what is your name": [
        "My name is ChatBot! Nice to meet you.",
        "I'm ChatBot, your AI assistant.",
        "You can call me ChatBot!"
    ],
    "what can you do": [
        "I can chat with you, answer basic questions, help with simple tasks, and keep you company!",
        "I'm here to help with conversations, answer questions, and assist you with various topics.",
        "I can engage in friendly conversation, answer questions, and help you with information."
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! It was nice chatting with you!"
    ],
    "thanks": [
        "You're welcome!",
        "No problem at all!",
        "Glad I could help!"
    ],
    "help": [
        "I can help you with:\n• General conversation\n• Basic questions\n• Information about various topics\n• Simple calculations\n• Weather information (if you tell me your location)\nJust type your message and I'll respond!",
        "Here's what I can do:\n• Chat and have conversations\n• Answer questions\n• Provide information\n• Help with simple tasks\nFeel free to ask me anything!",
        "I'm here to help! I can:\n• Engage in friendly conversation\n• Answer your questions\n• Provide information on various topics\n• Assist with simple tasks\nWhat would you like to know?"
    ]
}

# Function to get chatbot response
def get_bot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
    # Check for exact matches first
    for key in RESPONSES:
        if key in user_input_lower:
            return random.choice(RESPONSES[key])
    
    # Check for greetings
    greetings = ["hi", "hey", "good morning", "good afternoon", "good evening"]
    if any(greeting in user_input_lower for greeting in greetings):
        return random.choice(RESPONSES["hello"])
    
    # Check for farewells
    farewells = ["goodbye", "see you", "take care", "farewell"]
    if any(farewell in user_input_lower for farewell in farewells):
        return random.choice(RESPONSES["bye"])
    
    # Check for gratitude
    gratitude = ["thank", "thanks", "appreciate"]
    if any(grat in user_input_lower for grat in gratitude):
        return random.choice(RESPONSES["thanks"])
    
    # Check for questions about capabilities
    capability_questions = ["what can you do", "what do you do", "your capabilities", "your skills"]
    if any(cap in user_input_lower for cap in capability_questions):
        return random.choice(RESPONSES["what can you do"])
    
    # Check for time-related questions
    if "time" in user_input_lower:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    # Check for date-related questions
    if "date" in user_input_lower or "today" in user_input_lower:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date}."
    
    # Check for weather questions
    if "weather" in user_input_lower:
        return "I'd love to help with weather information! Please tell me your city or location."
    
    # Check for math questions
    if any(op in user_input_lower for op in ["calculate", "math", "plus", "minus", "multiply", "divide"]):
        return "I can help with basic calculations! Try asking something like 'calculate 5 + 3' or 'what is 10 * 2'."
    
    # Default responses for unknown queries
    default_responses = [
        "That's interesting! Tell me more about that.",
        "I'm not sure I understand. Could you rephrase that?",
        "Interesting question! I'm still learning, but I'd love to chat about other topics.",
        "I'm here to help! What else would you like to know?",
        "That's a good point! What's on your mind?",
        "I'm listening! What would you like to discuss?",
        "That's fascinating! I'd love to hear more.",
        "I'm here to chat and help! What else interests you?"
    ]
    
    return random.choice(default_responses)

# Simple math calculation function
def calculate_math(expression):
    try:
        # Replace words with operators
        expression = expression.lower()
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("multiply by", "*")
        expression = expression.replace("multiplied by", "*")
        expression = expression.replace("divide by", "/")
        expression = expression.replace("divided by", "/")
        
        # Extract numbers and operators
        import re
        numbers = re.findall(r'\d+', expression)
        operators = re.findall(r'[\+\-\*/]', expression)
        
        if len(numbers) >= 2 and len(operators) >= 1:
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            op = operators[0]
            
            if op == "+":
                return f"The answer is {num1 + num2}"
            elif op == "-":
                return f"The answer is {num1 - num2}"
            elif op == "*":
                return f"The answer is {num1 * num2}"
            elif op == "/":
                if num2 == 0:
                    return "Sorry, I can't divide by zero!"
                return f"The answer is {num1 / num2}"
    except:
        pass
    return None

# Main Streamlit app
def main():
    st.set_page_config(
        page_title="Simple Chatbot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("🤖 Simple Chatbot")
    st.markdown("---")
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This is a simple chatbot that can:
        - Have friendly conversations
        - Answer basic questions
        - Tell you the time and date
        - Help with simple calculations
        - Respond to greetings and farewells
        
        **Try saying:**
        - "Hello"
        - "What can you do?"
        - "What time is it?"
        - "Calculate 5 + 3"
        - "How are you?"
        """)
        
        st.markdown("---")
        st.markdown("**Built with:**")
        st.markdown("- Python")
        st.markdown("- Streamlit")
        st.markdown("- Natural Language Processing")
    
    # Main chat area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Display chat messages
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {message["content"]}
                    <small style="color: #666;">{message["timestamp"]}</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>ChatBot:</strong> {message["content"]}
                    <small style="color: #666;">{message["timestamp"]}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Input area
        st.markdown("---")
        user_input = st.text_input("Type your message here...", key="user_input", placeholder="Hello! How can I help you?")
        
        # Send button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Send", type="primary", use_container_width=True):
                if user_input.strip():
                    # Add user message to chat
                    timestamp = datetime.now().strftime("%H:%M")
                    st.session_state.messages.append({
                        "role": "user",
                        "content": user_input,
                        "timestamp": timestamp
                    })
                    
                    # Check for math calculations first
                    math_result = calculate_math(user_input)
                    if math_result:
                        bot_response = math_result
                    else:
                        # Get bot response
                        bot_response = get_bot_response(user_input)
                    
                    # Add bot response to chat
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": bot_response,
                        "timestamp": timestamp
                    })
                    
                    # Clear input
                    st.rerun()
    
    with col2:
        st.markdown("### Quick Actions")
        if st.button("👋 Say Hello"):
            st.session_state.user_input = "Hello"
            st.rerun()
        
        if st.button("❓ Ask for Help"):
            st.session_state.user_input = "Help"
            st.rerun()
        
        if st.button("⏰ Ask Time"):
            st.session_state.user_input = "What time is it?"
            st.rerun()
        
        if st.button("📅 Ask Date"):
            st.session_state.user_input = "What's today's date?"
            st.rerun()
        
        if st.button("🧮 Calculate"):
            st.session_state.user_input = "Calculate 10 + 5"
            st.rerun()
        
        st.markdown("---")
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main() 