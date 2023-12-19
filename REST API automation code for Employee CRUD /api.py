from flask import Flask, request, jsonify
from database import initialize_database, create_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee

app = Flask(__name__)

# Initialize the database
initialize_database()

# Create Employee
@app.route('/employees', methods=['POST'])
def create_employee_route():
    data = request.get_json()
    if not data or 'name' not in data or 'department' not in data or 'position' not in data:
        return jsonify({'error': 'Incomplete data'}), 400

    name = data['name']
    department = data['department']
    position = data['position']

    create_employee(name, department, position)

    return jsonify({'message': 'Employee created successfully'}), 201

# Read All Employees
@app.route('/employees', methods=['GET'])
def get_employees_route():
    employees = get_all_employees()
    return jsonify({'employees': employees})

# Read Employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_route(id):
    employee = get_employee_by_id(id)

    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    return jsonify({'employee': employee})

# Update Employee by ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee_route(id):
    data = request.get_json()
    if not data or 'name' not in data or 'department' not in data or 'position' not in data:
        return jsonify({'error': 'Incomplete data'}), 400

    name = data['name']
    department = data['department']
    position = data['position']

    update_employee(id, name, department, position)

    return jsonify({'message': 'Employee updated successfully'})

# Delete Employee by ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee_route(id):
    delete_employee(id)

    return jsonify({'message': 'Employee deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
