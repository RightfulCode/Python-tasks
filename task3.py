"""Python program to check whether the given integer is a multiple of 5"""

req_num = int(input("Enter any integer: \n"))

if req_num % 5 == 0:
    print(f"{req_num} is a multiple of 5")
else:
    print(f"{req_num} is not a multiple of 5")