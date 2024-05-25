num = int(input("Enter your Year: "))

if (num%400==0) or ((num%4==0) and (num%100!=0)):
    print("Leap Year")
else:
    print("Not a Leap Year")