user_data = input("Enter numbers separated by spaces: ")
list_data = [int(x) for x in user_data.split()]
print("Original:", list_data)

list_data.append(9)  
print("After append:", list_data)

list_data.insert(0, 7) 
print("After insert:", list_data)

list_data.remove(1)
print("After remove:", list_data)

list_data.sort()  
print("After sort:", list_data)

list_data.reverse()  
print("After reverse:", list_data)

