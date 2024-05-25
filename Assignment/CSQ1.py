'''
Largest among Three Numbers: 
Write a Python program that takes three numbers as input 
and prints out the largest among them.
'''

# Input three numbers
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))

# Show three numbers
print(f"Your have entered: {num1}, {num2} & {num3}")

if (num1>num2) and (num1>num3):
    print(f"{num1} is the largest number ") 
elif (num2>num1) and (num2>num3):
    print(f"{num2} is the largest number ") 
else:
    print(f"{num3} is the largest number ")  