# db_operations.py

import mysql.connector
import json

# MySQL database configuration
def load_db_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        db_config = config.get('db_config', {})
    return db_config

# Function to establish a database connection
def connect_to_database():
   db_config = load_db_config()
   return mysql.connector.connect(**db_config)

def create_employee_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        department VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

# Function to get all employees from the database
def get_employees():
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

# Function to get a specific employee by ID from the database
def get_employee(id):
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee

# Function to add an employee to the database
def add_employee(name, department):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO employee (name, department) VALUES (%s, %s)"
    values = (name, department)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    new_employee_id = cursor.lastrowid
    return new_employee_id

# Function to update an employee in the database by ID
def update_employee(id, name, department):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "UPDATE employee SET name = %s, department = %s WHERE id = %s"
    values = (name, department, id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

# Function to delete an employee from the database by ID
def delete_employee(id):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "DELETE FROM employee WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
