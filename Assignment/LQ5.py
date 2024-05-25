'''
Print the pattern (for/while):
1
22
333
4444
55555
'''

# Using a for loop to print the pattern
print("Using 'for' loop:")
for i in range(1, 6):
    print(str(i) * i)

# blank line in the output
print("\n") 

# Using a While loop to print the pattern
print("Using 'While' loop:")
i = 1
while i <= 5:
    print(str(i) * i)
    i += 1




