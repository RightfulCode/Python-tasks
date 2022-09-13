"""Python program to add a key to a dictionary"""

this_dict = {
    0:10,
    1:20,
}

key = int(input("Enter the key: \n"))
value = int(input("Enter the value: \n"))

this_dict[key] = value
print(this_dict)