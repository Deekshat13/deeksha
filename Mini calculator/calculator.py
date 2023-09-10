# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to log calculation history
def log_history(num1, operation, num2, result):
    with open("calculator_results.txt", "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")

# Function to perform calculations
def calculator():
    while True:
        operation = input("Enter operation (+, -, *, /, exit, history):")

        if operation in ("+", "-", "*", "/"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)

            print(result)
            log_history(num1, operation, num2, result)

        elif operation == "exit":
            print("Exiting calculator.")
            break

        elif operation == 'history':
            file_path = 'calculator_results.txt'  # Replace 'your_file.txt' with the actual file path

            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        print(line, end='')  # Use end='' to avoid adding extra line breaks

            except FileNotFoundError:
                print(f"File '{file_path}' not found.")

            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("Invalid input")

# Call the calculator function to start the calculator
if __name__ == "__main__":
    calculator()
