'''
Quadrant Identifier: 
Write a Python program that takes the coordinates 
(x, y) of a point as input and prints out 
which quadrant it belongs to (1st, 2nd, 3rd, or 4th.
'''

# Conditions to Check Quadrants
# If x > 0 and y > 0: The point is in the 1st Quadrant.
# If x < 0 and y > 0: The point is in the 2nd Quadrant.
# If x < 0 and y < 0: The point is in the 3rd Quadrant.
# If x > 0 and y < 0: The point is in the 4th Quadrant.
# If x == 0 and y == 0: The point is at the Origin.
# If x == 0: The point is on the Y-axis.
# If y == 0: The point is on the X-axis.

# Input coordinates
x = eval(input("Enter the x-coordinate: "))
y = eval(input("Enter the y-coordinate: "))


if x > 0 and y > 0:
    print(f"{x} & {y} points belongs to the 1st Quadrant.")
elif x < 0 and y > 0:
    print(f"{x} & {y} points belongs to the 2nd Quadrant.")
elif x < 0 and y < 0:
    print(f"{x} & {y} point belongs to the 3rd Quadrant.")
elif x > 0 and y < 0:
    print(f"{x} & {y} points belongs to the 4th Quadrant.")
elif x == 0 and y == 0:
    print(f"{x} & {y} points lies at the Origin.")
elif x == 0:
    print(f"{x} & {y} points lies on the Y-axis.")
elif y == 0:
    print(f"{x} & {y} points lies on the X-axis.")
