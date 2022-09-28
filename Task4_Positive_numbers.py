#Write a Python program to print all positive numbers in a range.
#Your Input and output must look something like this
#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
#Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]

# Python program to print positive Numbers in a List

# list of numbers
list1 = [12, -7, 5, 64, -14]
list2= [12, 14, -95, 3]


def positive_num(list):
    # using while loop
    num = 0

    while(num < len(list)):

        # checking condition
        if list[num] >= 0:
            print(list[num], end = " ")

        # increment num
        num += 1

#Printing the output
print("Postive Numbers in List 1: [12, -7, 5, 64, -14] are :")
positive_num(list1)
print("\n\nPostive Numbers in List 1: [12, 14, -95, 3] are :")
positive_num(list2)
