n = int(input("Enter N (print 1 to N, skip even numbers): "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"Skipping even numbers {i} with continue")
        continue
    print(f"for loop odd number = {i}")
