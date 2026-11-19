def simple_interest(principal, time, rate=5):  
    return (principal * time * rate) / 100

print("SI (default rate):", simple_interest(4000, 3))    
print("SI (rate=8):", simple_interest(3000, 3, 8))       