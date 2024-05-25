'''
FizzBuzz: 
Write a Python program that prints the numbers from 1 to 100. 
But for multiples of three, print "Fizz" instead of the number, 
and for the multiples of five, print "Buzz". 
For numbers that are multiples of both three and five, 
print "FizzBuzz" using a for loop.
'''

# Loop through numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of 5
    elif num % 5 == 0:
        print("Buzz")
    # If not a multiple of 3 or 5, print the number
    else:
        print(num)


