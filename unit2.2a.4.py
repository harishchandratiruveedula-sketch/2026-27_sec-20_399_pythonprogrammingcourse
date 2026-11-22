marks = int(input("Enter marks: "))

if marks >= 90:
    print(f"marks {marks}: Grade A")
elif 80 <= marks < 90:
    print(f"marks {marks}: Grade B")
elif 70 <= marks < 80:
    print(f"marks {marks}: Grade C")
elif 60 <= marks < 70:
    print(f"marks {marks}: Grade D")
else:
    print(f"marks {marks}: Grade F")
