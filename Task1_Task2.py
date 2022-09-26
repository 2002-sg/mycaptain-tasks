"""Task 1 --> Write a Python program which accepts the radius of a circle from the user and computes area."""
r = float(input("Enter radius of circle: "))
a = 3.141592653589793238 * r * r
print("Area of circle =", a)

"""Task 2 -->  Write a Python program to accept a filename from the user and print the extension of that."""

filename = input("Input the Filename: ")
file_ext = filename.split(".")
print ("The extension of the file is : " + repr(file_ext[-1]))
