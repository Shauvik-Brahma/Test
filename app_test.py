import streamlit as st
import mysql.connector

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',                 # Replace with your MySQL username
    'password': 'Shau@123',     # Replace with your MySQL password
    'database': 'office'
}

# Connect to MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
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
            print("Record successfully added to the database!")
        except mysql.connector.Error as err:
            print(f"Failed to insert record: {err}")
        finally:
            cursor.close()
            conn.close()

# Main code to input employee details
def main():
    print("Enter employee details:")

    # Get user input
    employee_id = int(input("Employee ID: "))
    department = input("Department: ")
    hire_date = input("Hire Date (YYYY-MM-DD): ")
    salary = float(input("Salary: "))

    # Insert the employee data into the database
    insert_employee(employee_id, department, hire_date, salary)

if __name__ == "__main__":
    main()
