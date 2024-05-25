# Input from the user
ch = input("Enter any character: ")

# Convert the input character to lowercase
ch = ch.lower()

# Check if the character is an alphabetic letter
if not ch.isalpha():
    print("This is not an alphabetic character")
elif (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("This is a Vowel")
else:
    print("This is a Consonant")
