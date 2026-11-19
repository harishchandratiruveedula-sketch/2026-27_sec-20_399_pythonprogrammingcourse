user_data = input("Enter numbers separated by spaces: ")
list_data = [int(x) for x in user_data.split()]
print("Original:", list_data)
unique = []                       
for item in list_data:          
    if item not in unique:         
        unique.append(item)     
print("Without duplicates:", unique)