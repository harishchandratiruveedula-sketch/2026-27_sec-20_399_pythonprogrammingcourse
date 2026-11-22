P = float(input("Enter the principal in rupees: "))
R = float(input("Enter the rate of interest in percent: "))
T = float(input("Enter time in years: "))
compound_interest = P * (1 + R / 100) ** T
print(compound_interest)