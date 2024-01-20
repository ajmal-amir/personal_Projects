def shift_lowercase_to_front(input_string):
    lowercase_letters = ""
    uppercase_letters = ""

    for char in input_string:
        if char.islower():
            lowercase_letters += char
        elif char.isupper():
            uppercase_letters += char

    result_string = lowercase_letters + uppercase_letters

    print("Result:", result_string)

# Get input from the user
user_input = input("Enter a string: ")

# Call the function with the user input
shift_lowercase_to_front(user_input)
