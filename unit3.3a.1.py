user_input = input("Enter numbers separated by spaces: ")
list_data = [int(x) for x in user_input.split()]
print("List:", list_data)
for item in list_data:
    print(item)