import streamlit as st
import re

# Streamlit UI setup
st.title("Password Strength Meter 💻📈")

# Password history (in-memory for now)
if 'password_history' not in st.session_state:
    st.session_state.password_history = []

# Password Input (show history suggestions)
password = st.text_input("Enter your password:", 
                         value="", 
                         placeholder="Type your password",
                         help="You can reuse previous passwords from history.")

# Show password history as suggestions
if st.session_state.password_history:
    # Show past passwords in a dropdown menu below the input field
    history_suggestions = st.selectbox("your Password history", 
                                       options=[""] + st.session_state.password_history,
                                       index=0,  # Default to no selection
                                       help="Select a previous password or keep typing.")
    if history_suggestions:
        password = history_suggestions

# Display password guidelines only after the user starts typing
if password:
    # Sidebar with instructions and suggestions after password input
    st.sidebar.title("Password Guidelines")
    st.sidebar.markdown("""
        **Password should include the following:**
        - ❌ Password should be at least 8 characters long.
        - ❌ Include both uppercase and lowercase letters.
        - ❌ Add at least one number (0-9).
        - ❌ Include at least one special character (!@#$%^&*).
        
        **Weak Password** - Improve it using the suggestions above.
    """)

    # Function to check password strength
    def check_password_strength(password):
        score = 0
        feedback = []

        # Length Check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        # Upper & Lowercase Check
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Include both uppercase and lowercase letters.")

        # Digit Check
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ Add at least one number (0-9).")

        # Special Character Check
        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append("❌ Include at least one special character (!@#$%^&*).")

        # Strength Rating and Feedback
        if score == 4:
            st.write("✅ Strong Password!")
        elif score == 3:
            st.write("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.write("❌ Weak Password - Improve it using the suggestions above.")
        
        # Show feedback suggestions
        if feedback:
            for line in feedback:
                st.write(line)

        # Calculate security percentage
        security_percentage = (score / 4) * 100
        st.write(f"🔒 Security Rating: {security_percentage:.0f}%")

        # Track the password history
        st.session_state.password_history.append(password)

    # Check password strength
    check_password_strength(password)

else:
    # Show the instructions before entering a password
    st.sidebar.title("Password Guidelines")
    st.sidebar.markdown("""
        **Password should include the following:**
        - Password should be at least 8 characters long.
        - Include both uppercase and lowercase letters.
        - Add at least one number (0-9).
        - Include at least one special character (!@#$%^&*).
        
        **Weak Password** - Improve it using the suggestions above.
    """)