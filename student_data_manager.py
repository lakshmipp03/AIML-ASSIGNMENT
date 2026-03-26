# Student Data Manager

students = {
    "Aman": 85,
    "Sara": 92,
    "Rahul": 74,
    "Neha": 68,
    "Arjun": 88
}

# Find topper
topper = max(students, key=students.get)

# Calculate class average
average = sum(students.values()) / len(students)

print("Student Marks:", students)
print("Topper:", topper, "-", students[topper])
print("Class Average:", round(average, 2))

print("\nGrades:")

for student, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print(student, ":", grade)