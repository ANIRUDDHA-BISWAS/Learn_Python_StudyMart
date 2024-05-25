# fibonacci series

# Number of terms we want in the Fibonacci series
num_terms = int(input("Enter Your Number: "))

# Starting values
n1 = 0
n2 = 1
count = 0

if num_terms <=0:
    print('Invalid Input')
elif num_terms ==1:
    print(n1)
else:
# count Fibonacci series
    while count < num_terms:
        print(n1, end=' ')
        nxt_term = n1 + n2
        n1=n2
        n2=nxt_term
        count += 1
