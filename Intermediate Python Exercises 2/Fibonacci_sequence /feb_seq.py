import time
import random


def fibonacci(n):
    if n <= 0: 
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2: 
        return 1
    else:
        a, b = 0, 1
        for _ in range(n -2):
            a, b = b, a + b
        return b
    
# Generateing a random number between 15 and 35
random_n = random.randint(15, 35)

# Time the excution of the fibonacci function 

start_time = time.time()
result = fibonacci(random_n)
end_time = time.time()

excution_time = end_time - start_time
# Print the result and excution tiem
print()
print("*************************************")
print(f"Fibonacci: ({random_n} = {result})")
print("*************************************")
print()
print("######################################################")
print(f"Execution time: {end_time - start_time} seconds")
print("######################################################")