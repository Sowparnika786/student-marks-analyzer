n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

    if m >= 90:
        grade = "A"
    elif m >= 75:
        grade = "B"
    elif m >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student {i+1}: {m} → {grade}")

print("\nClass Summary")
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks)/n)
