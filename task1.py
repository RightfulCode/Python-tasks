"""Python program to check whether the given number is even or not"""

req_number = int(input("Enter any integer: \n"))

if req_number % 2 == 0:
    print(f"{req_number} is even")
else:
    print(f"{req_number} is odd")