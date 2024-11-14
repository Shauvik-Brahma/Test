import streamlit as st
import mysql.connector
import time

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'Shau@123',  # Replace with your MySQL password
    'database': 'office'
}

# Predefined credentials for demo purposes
USERNAME = 'user'
PASSWORD = 'password123'

# Function to check login credentials
def check_credentials(username, password):
    return username == USERNAME and password == PASSWORD

# Connect to MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            st.success("Connected to the database")
            return conn
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Insert data into MySQL database
def insert_employee(employee_id, department, hire_date, salary):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO Employee_Test (EmployeeID, Department, HireDate, Salary)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (employee_id, department, hire_date, salary))
            conn.commit()
            st.success("Record successfully added to the database!")
        except mysql.connector.Error as err:
            st.error(f"Failed to insert record: {err}")
        finally:
            cursor.close()
            conn.close()

# Login page
def login_page():
    st.title("Login Page")

    # Get user inputs for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check login credentials
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Login successful!")
            st.write("Redirecting to Employee Insertion page...")
            time.sleep(1)  # Wait for a second before redirecting
            employee_insertion_page()  # Call the employee insertion function
        else:
            st.error("Invalid credentials. Please try again.")

# Employee insertion page
def employee_insertion_page():
    st.title("Employee Data Insertion")

    # Get user input using Streamlit widgets
    employee_id = st.number_input("Employee ID", min_value=1, step=1)
    department = st.text_input("Department")
    hire_date = st.date_input("Hire Date")
    salary = st.number_input("Salary", min_value=0.0, step=1000.0)

    # Button to submit data
    if st.button("Submit"):
        if employee_id and department and hire_date and salary:
            insert_employee(employee_id, department, str(hire_date), salary)
        else:
            st.warning("Please fill all fields")

if __name__ == "__main__":
    login_page()  # Show login page first