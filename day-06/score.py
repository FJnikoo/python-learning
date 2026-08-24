students = [
    {"name": "Ali", "score": 85 },
    {"name": "Sara", "score": 92 },
    {"name": "Robert", "score": 60 }
]
for student in students:
    if student['score'] >= 80:
        print(student["name"])
