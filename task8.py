"""Python program to find the smallest number among three"""

num_list = []

num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))
num3 = int(input("Enter third number: \n"))

num_list[:] = [num1,num2,num3]
num_list.sort()

print(f"Smallest number is {num_list[0]}")