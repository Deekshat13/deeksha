# Define a function to check number
def check_number(number):
    # Check if the score is more than or equal to 70
    if number >= 70:
        return "You have passed"
    else:
        return "You have not passed"

# Define the number
number = 70

# Call the function to check the result and print it
result = check_number(number)
print(result)
