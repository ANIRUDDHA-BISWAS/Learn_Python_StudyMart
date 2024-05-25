'''
Age Classifier: 
Write a Python program that takes a person's age as input and 
prints out whether they are an infant (0-1), toddler (1-3), 
child (4-12), teenager (13-19), adult (20+).
'''

# Input the person's age
age = int(input("Enter the age: "))

if age >= 20:
    print("The person is an adult.")
elif age < 20 and age >= 13:
    print("The person is a teenager.")  
elif age <= 12 and age >= 4:
    print("The person is a child.")
elif age <= 3 and age > 1:
    print("The person is a toddler.")  
else:
    print("The person is an infant.")



  