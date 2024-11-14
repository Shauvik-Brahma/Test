import streamlit as st

# Predefined credentials for demo purposes
USERNAME = 'user'
PASSWORD = 'password123'

# Function to check login credentials
def check_credentials(username, password):
    return username == USERNAME and password == PASSWORD

# Streamlit page layout
def login_page():
    st.title("Login Page")

    # Get user inputs for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check login credentials
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Login successful!")
            st.write("Welcome to the main page.")
            # Redirect or call another function here (e.g., main app function)
            main_page()  # This can be your actual app function
        else:
            st.error("Invalid credentials. Please try again.")

# Main page content (will be shown after successful login)
def main_page():
    st.title("Main App")
    st.write("This is the main app content that users will see after logging in.")
    # You can put your main app functionality here

if __name__ == "__main__":
    login_page()
