x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x < y and x < z:
    smallest = x
elif y < x and y < z:
    smallest = y
else:
    smallest = z
print(smallest)