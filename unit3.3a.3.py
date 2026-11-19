user_data = input("Enter numbers separated by spaces: ")
list_data = [int(x) for x in user_data.split()]
print("Original:", list_data)
print(max(list_data))
print(min(list_data))