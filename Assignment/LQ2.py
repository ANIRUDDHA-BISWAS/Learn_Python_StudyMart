'''
Armstrong Number Checker: 
Write a Python program that takes an integer 
input from the user and checks if it is an Armstrong number 
(a number that is equal to the sum of its own digits raised 
to the power of the number of digits) using a for loop.
'''

# Input an integer from the user
number = int(input("Enter an integer: "))

# Convert the number to a string to easily access each digit
num_str = str(number)

# Calculate the number of digits
num_digits = len(num_str)

# Initialize a variable to store the sum of the digits raised to the power of num_digits
sum_of_powers = 0

# Loop through each digit in the number
for digit in num_str:
    # Convert the digit back to an integer and raise it to the power of num_digits, then add to sum_of_powers
    sum_of_powers += int(digit) ** num_digits

# Check if the sum of the powers is equal to the original number
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

    