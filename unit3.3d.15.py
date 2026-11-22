def total_and_average(mark_1, mark_2, mark_3):
    total = mark_1 + mark_2 + mark_3
    average = (mark_1 + mark_2 + mark_3) / 3 
    return total, average

m1 = int(input("Enter first number: "))
m2 = int(input("Enter second number: "))
m3 = int(input("Enter third number: "))


total, average = total_and_average(m1, m2, m3)

print("total :", total)
print("average :", average)