'''
Number Reverser: 
Write a Python program that takes an integer input 
from the user and prints its reverse using a while loop.
'''

# Input an integer from the user
number = int(input("Enter an integer: "))

# Initialize the variable to store the reversed number
reversed_number = 0

# Store the original number for output
original_number = number

# Loop to reverse the number
while number != 0:
    # Get the last digit of the number
    digit = number % 10
    # Add the digit to the reversed_number (shift digits left by multiplying by 10)
    reversed_number = reversed_number * 10 + digit
    # Remove the last digit from the number
    number = number // 10

# Print the reversed number
print(f"The reverse of {original_number} is {reversed_number}.")
