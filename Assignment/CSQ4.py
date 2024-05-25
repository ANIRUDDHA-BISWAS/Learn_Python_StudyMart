'''
BMI Calculator: 
Write a Python program that takes a person's height (in meters) 
and weight (in kilograms) as input and calculates their Body Mass Index (BMI).
Print out their BMI and a message indicating whether they are 
underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (>=30).
'''

# Determine the BMI category
# If BMI is less than 18.5: Underweight
# If BMI is between 18.5 and 24.9 (inclusive): Normal weight
# If BMI is between 25 and 29.9 (inclusive): Overweight
# If BMI is 30 or above: Obese


# Input the person's height in meters
height = float(input("Enter the height in meters: "))
# Input the person's weight in kilograms
weight = float(input("Enter the weight in kilograms: "))

# Calculate BMI
BMI = weight / (height ** 2)

# Round the BMI to two decimal places
BMI = round(BMI, 2)

# Print the BMI value
print(f"Your BMI is: {BMI}")

if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You have a normal weight.")
elif 25 <= BMI <= 29.9:
    print("You are overweight.")
elif BMI >= 30:
    print("You are obese.")
