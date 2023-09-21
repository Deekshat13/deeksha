# Define a function to get user input for numbers and words
def get_user_input():
    numbers = []
    words = []

    while True:
        user_input = input("Enter a number or a word (0 or END to stop): ")

        if user_input == "0" or user_input.lower() == "end":
            break

        if user_input.isdigit():  # Check if the input is a number
            #num = int(user_input)
            numbers.append(user_input)
        else:
            words.append(user_input)

    return numbers, words

# Define a function to sort and print a list of items
def sort_and_print(items):
    if items:
        ascending_items = sorted(items)
        descending_items = sorted(items, reverse=True)
        print("Items in ascending order:", ascending_items)
        print("Items in descending order:", descending_items)
    else:
        print("No items were entered.")

if __name__ == "__main__":
    # Get user input for numbers and words
    numbers, words = get_user_input()

    # Sort and print the numbers
    sort_and_print(numbers)

    # Sort and print the words
    sort_and_print(words)
