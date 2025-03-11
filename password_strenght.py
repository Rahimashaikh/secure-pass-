import streamlit as st
import string
import random
import re
import base64
import os

# Set page config
st.set_page_config(page_title="SecurePass Pro", page_icon="🔐", layout="wide")

# Override Streamlit's default styles with custom CSS
st.markdown("""
<style>
/* Force all input text to be black regardless of theme */
.stTextInput input {
    color: black !important;
    background-color: white !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

# Function to load and encode the image
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Get the image path
image_path = os.path.join("Streamlit_Project", "download (1).jpeg")
background_image = get_base64_encoded_image(image_path)

# Custom CSS styling with the background image and responsive design
st.markdown(f"""
    <style>
    /* Base styling */
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    
    /* Main background and container styling */
    .stApp {{
        background-image: linear-gradient(135deg, rgba(26, 26, 46, 0.9) 0%, rgba(22, 33, 62, 0.9) 100%),
                         url("data:image/jpeg;base64,{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;
        max-width: 100vw;
        overflow-x: hidden;
    }}
    
    /* Container styling */
    .main {{
        padding: 2rem;
        border-radius: 10px;
        background-color: rgba(26, 26, 46, 0.7);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 100%;
        margin: 0 auto;
    }}
    
    /* Title styling */
    h1 {{
        color: #ffffff !important;
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        font-size: calc(1.5rem + 1vw);
        line-height: 1.3;
    }}
    
    h1 span {{
        font-size: calc(1rem + 0.5vw);
        display: block;
        margin-top: 0.5rem;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, #4ecca3, #45b392);
        color: #1a1a2e;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background: linear-gradient(135deg, #45b392, #4ecca3);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(78, 204, 163, 0.3);
    }}
    
    /* Input fields */
    .stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.2);
        color: #e0e0e0;
        border: 1px solid #4ecca3;
        font-weight: bold;
        width: 100%;
        padding: 0.75rem;
    }}
    
    /* Password input specific styling */
    input[type="password"] {{
        color: #00ff00 !important; /* Bright green color for password text */
        letter-spacing: 0.2em; /* Add spacing between characters for better visibility */
        font-weight: bold;
    }}
    
    /* Tabs styling */
    .stTabs > div > div > div {{
        background-color: rgba(26, 26, 46, 0.8);
        border-radius: 5px;
        padding: 10px;
        border: 1px solid rgba(78, 204, 163, 0.2);
        overflow-x: auto;
    }}
    
    .stTab {{
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        flex: 1;
        text-align: center;
        min-width: 120px;
    }}
    
    .stTab[aria-selected="true"] {{
        background-color: #4ecca3;
        color: #1a1a2e;
    }}
    
    /* Progress bar */
    .stProgress > div > div > div > div {{
        background-color: #4ecca3;
    }}
    
    /* Text colors */
    .stMarkdown, p, label {{
        color: white !important;
    }}

    /* Code block styling */
    .stCodeBlock {{
        background-color: rgba(26, 26, 46, 0.8) !important;
        border: 1px solid #4ecca3;
        overflow-x: auto;
        word-break: break-word;
    }}

    /* Slider styling */
    .stSlider {{
        background-color: rgba(26, 26, 46, 0.8);
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid rgba(78, 204, 163, 0.2);
    }}
    
    /* Footer styling */
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(26, 26, 46, 0.9);
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        border-top: 1px solid #4ecca3;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.2);
        z-index: 999;
    }}
    
    .footer-content {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }}
    
    .footer-text {{
        margin: 0 10px;
    }}
    
    .developer-name {{
        color: #4ecca3;
        font-weight: bold;
    }}
    
    /* Column Layouts */
    .column-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 1rem;
    }}
    
    .column {{
        flex: 1;
        min-width: 250px;
    }}
    
    /* Media Queries for Responsive Design */
    @media screen and (max-width: 768px) {{
        .main {{
            padding: 1rem;
        }}
        
        h1 {{
            font-size: 1.5rem;
            padding: 0.5rem;
            margin-bottom: 1rem;
        }}
        
        h1 span {{
            font-size: 1rem;
        }}
        
        .stButton > button {{
            padding: 0.5rem 1rem;
        }}
        
        .column {{
            min-width: 100%;
        }}
        
        .footer-text {{
            font-size: 12px;
        }}
    }}
    
    @media screen and (max-width: 480px) {{
        h1 {{
            font-size: 1.2rem;
        }}
        
        h1 span {{
            font-size: 0.9rem;
        }}
        
        .stTab {{
            min-width: 100px;
            padding: 0.3rem;
        }}
        
        .footer-text {{
            margin: 0 5px;
            font-size: 10px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Contains number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number")
    
    # Contains lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter")
    
    # Contains uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")
    
    # Contains special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character")
    
    # Strength level
    if score <= 2:
        strength = "Weak"
        color = "#ff6b6b"
    elif score <= 4:
        strength = "Medium"
        color = "#ffd93d"
    else:
        strength = "Strong"
        color = "#4ecca3"
    
    return score, strength, color, feedback

def generate_password(length=12, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*(),.?\":{}|<>"
    
    # Create the character pool
    char_pool = letters
    if use_numbers:
        char_pool += digits
    if use_symbols:
        char_pool += symbols
    
    # Generate password ensuring at least one character from each selected type
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    
    if use_numbers:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(char_pool))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def main():
    # Create a container for better layout control
    container = st.container()
    
    with container:
        # Custom HTML for two-line title
        st.markdown("""
            <h1>
                🔐 SecurePass
                <span>Strength & Password Check Pro 🏅</span>
            </h1>
        """, unsafe_allow_html=True)
        
        # Wrap content in a centered column
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col2:
            tabs = st.tabs(["Generate Password", "Check Password"])
            
            with tabs[0]:
                st.subheader("Generate a Strong Password")
                
                col1, col2 = st.columns(2)
                with col1:
                    length = st.slider("Password Length", 8, 32, 12)
                with col2:
                    st.write("")
                    st.write("")
                    use_numbers = st.checkbox("Include Numbers", value=True)
                    use_symbols = st.checkbox("Include Symbols", value=True)
                
                if st.button("Generate Password"):
                    password = generate_password(length, use_numbers, use_symbols)
                    st.code(password)
                    
                    # Show password strength
                    score, strength, color, feedback = check_password_strength(password)
                    st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
                    st.progress(score/5)
            
            with tabs[1]:
                st.subheader("Check Your Password")
                # Custom password input with black text
                password = st.text_input(
                    "Enter your password", 
                    type="password"
                )
                
                if password:
                    score, strength, color, feedback = check_password_strength(password)
                    
                    st.markdown(f"**Password Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
                    st.progress(score/5)
                    
                    if feedback:
                        st.warning("Improvements needed:")
                        for suggestion in feedback:
                            st.markdown(f"- {suggestion}")
                    else:
                        st.success("Your password meets all security requirements!")

    # Add footer at the end of the application
    st.markdown("""
        <div class="footer">
            <div class="footer-content">
                <p class="footer-text">© 2025 SecurePass Pro | Developed by <span class="developer-name">Rahima Shaikh</span></p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add a spacer at the bottom to prevent content from being hidden behind the footer
    st.markdown("<div style='padding-bottom: 70px;'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 