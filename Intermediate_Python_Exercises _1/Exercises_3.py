def count_letters(input_string):
    # Initialize an empty dictionary to store letter counts
    letter_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Exclude spaces and consider only lowercase letters
        if char.isalpha() and char.islower():
            # Increment the count for the current letter in the dictionary
            letter_count[char] = letter_count.get(char, 0) + 1

    # Return the dictionary containing letter counts
    return letter_count

# Get input from the user
user_input = input("Enter a string: ")

# Call the count_letters function with the user input
result_dict = count_letters(user_input)

# Print the dictionary containing letter counts
print(result_dict)
