#The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.


# Write a Python Program for Fibonacci numbers.

nterms = int(input("Fibonacci sequence to be displayed for: "))

# first two terms
n1, n2 = 0, 1
ncount = 0

# Checking for a value ,needed to be a positive number
if nterms <= 0:
   print("Please enter a positive integer")
# For a single term,returning n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generating fibonacci sequence
else:
   print("Fibonacci sequence:")
   while ncount < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       ncount += 1
