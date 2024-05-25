'''
Temperature Converter: 
Write a Python program that takes a temperature input in Celsius 
and converts it to Fahrenheit if the temperature is above 0°C, 
or to Kelvin if the temperature is below 0°C.
'''

# Input temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Conversion formulas
# Celsius to Fahrenheit: (C * 9/5) + 32
# Celsius to Kelvin: C + 273.15

# Determine the conversion based on the temperature
if celsius > 0:
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
elif celsius < 0:
    kelvin = celsius + 273.15
    print(f"The temperature in Kelvin is: {kelvin:.2f} K")
else:
    print("The temperature is exactly 0°C, which is 32°F or 273.15 K")


    
