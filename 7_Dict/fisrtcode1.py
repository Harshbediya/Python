students = {
	"Aman": {"age": 20, "course": "Python", "marks": 85},
	"Neha": {"age": 21, "course": "Java", "marks": 92},
}

print("Student records:")
for name, details in students.items():
	print(name, "-", details)

# Add a new student.
students["Ravi"] = {"age": 19, "course": "C++", "marks": 78}

# Update an existing student's marks.
students["Aman"]["marks"] = 90

# Search safely for a student.
student_name = input("Enter a student name: ").strip()
student = students.get(student_name)

if student is None:
	print("Student not found")
else:
	print("Name:", student_name)
	print("Age:", student["age"])
	print("Course:", student["course"])
	print("Marks:", student["marks"])
