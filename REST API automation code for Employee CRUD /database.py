import sqlite3


def initialize_database():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  department TEXT NOT NULL,
                  position TEXT NOT NULL
                  )''')
    conn.commit()
    conn.close()


def create_employee(name, department, position):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, department, position) VALUES (?, ?, ?)', (name, department, position))
    conn.commit()
    conn.close()


def get_all_employees():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()

    employee_list = []
    for emp in employees:
        employee_list.append({
            'id': emp[0],
            'name': emp[1],
            'department': emp[2],
            'position': emp[3]
        })

    return employee_list


def get_employee_by_id(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (id,))
    employee = cursor.fetchone()
    conn.close()

    if not employee:
        return None

    employee_data = {
        'id': employee[0],
        'name': employee[1],
        'department': employee[2],
        'position': employee[3]
    }

    return employee_data


def update_employee(id, name, department, position):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET name = ?, department = ?, position = ? WHERE id = ?',
                   (name, department, position, id))
    conn.commit()
    conn.close()


def delete_employee(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
