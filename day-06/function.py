students = [
    {"name": "Ali", "score": 85 },
    {"name": "Sara", "score": 92 },
    {"name": "Robert", "score": 60 }
]
def show_students(students):
    for student in students:
       print(f"Name: {student['name']} | Score: {student['score']}")

show_students(students)
