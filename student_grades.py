students = {
    "Rahul": "A",
    "Amit": "B",
    "Priya": "A"
}

print("Student Grades:")
print(students)


name = input("Enter new student name: ")
grade = input("Enter student grade: ")

if name in students:
    print("Student already exists!")
else:
    students[name] = grade
    print("Student added successfully!")

print(students)


update_name = input("Enter student name to update: ")

if update_name in students:
    new_grade = input("Enter new grade: ")
    students[update_name] = new_grade
    print("Grade updated successfully!")
else:
    print("Student not found!")

print(students)


print("\nAll Student Grades:")

for name, grade in students.items():
    print(name, ":", grade)
