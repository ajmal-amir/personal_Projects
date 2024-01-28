# Define a function named get_unique_list that takes a list as input
def get_unique_list(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Iterate through each item in the input list
    for item in input_list:
        # Check if the item is not already in the unique_list
        if item not in unique_list:
            # If not, add the item to the unique_list
            unique_list.append(item)
    
    # Return the list containing unique elements
    return unique_list

# Test the function
# Create a list with duplicate and unique elements
my_list = [1, 2, 3, 2, 1, 4]
# Call the get_unique_list function with the test list
unique_list = get_unique_list(my_list)
# Print the result, which should be a list with unique elements
print(unique_list)
