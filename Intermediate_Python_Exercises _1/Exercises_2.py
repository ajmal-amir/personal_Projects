# Define a function named get_combined_dict that takes two dictionaries as input
def get_combined_dict(dict1, dict2):
    # Create an empty dictionary to store combined values
    combined_dict = {}
    
    # Find the common keys between dict1 and dict2
    common_keys = set(dict1.keys()) & set(dict2.keys())

    # Iterate through the common keys
    for key in common_keys:
        # Combine the values for common keys and store in the combined_dict
        combined_dict[key] = dict1[key] + dict2[key]

    # Return the dictionary containing combined values for common keys
    return combined_dict

# Test the function
# Create two dictionaries with some common and some unique keys
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
# Call the get_combined_dict function with the test dictionaries
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
# Print the result, which should be a dictionary with combined values for common keys
print(combined_dict)
