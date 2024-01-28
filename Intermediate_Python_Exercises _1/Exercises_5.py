# Define a function named sum_of_numbers that takes a list of numbers as input
def sum_of_numbers(nums):
    # Initialize an empty list to store the numbers
    num_list = []

    # Iterate through each number in the input list
    for number in nums:
        # Append the current number to the list
        num_list.append(number)
        # Calculate the sum of the numbers in the list
        result = sum(num_list)

    # Return the sum of the numbers
    return result


# Set the initial value for the number of inputs left to 5
numbers_left = 5
# Initialize an empty list to store user inputs
user_inputs = []
print("Please enter 5 ints")
# Start a loop that continues until all 5 inputs are received
while numbers_left > 0:
    try:
        # Attempt to get an integer input from the user
        user_input = int(input(f"Enter int #{numbers_left}: "))
        # Decrement the count of numbers left to be entered
        numbers_left -= 1
        # Append the user input to the list of user_inputs
        user_inputs.append(user_input)
    except ValueError as e:
        # Handle the case where the user enters a non-integer
        print("Please Enter an int. ")

# Call the sum_of_numbers function with the list of user inputs
result_of_sum = sum_of_numbers(user_inputs)
# Print the sum of the entered integers
print(f"Sum of the entered integers: {result_of_sum}")
