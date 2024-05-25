'''
Sum of Digits: 
Write a Python program that takes an integer input 
from the user and calculates the sum of its digits using a while loop.
'''

# Input an integer from the user
number = int(input("Enter an integer: "))

# Initialize the variable to store the sum of digits
sum_of_digits = 0

# Store the original number for reference
original_number = number

# Loop to calculate the sum of digits
while number != 0:
    # Get the last digit of the number
    digit = number % 10
    # Add the digit to the sum_of_digits
    sum_of_digits += digit
    # Remove the last digit from the number
    number = number // 10

# Print the sum of the digits
print(f"The sum of the digits of {original_number} is {sum_of_digits}.")