def show_students(students):
    for student in students:
        result = check_score(student["score"])
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Country: {student['country']}")
        print(f"Result: {result}")
        print(f"Score: {student['score']}")

def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

students = []
numb = int(input("how many students are? "))
for i in range(numb):
    name = input("Enter your name: ").capitalize()
    age = int(input("Enter your age: "))
    score = int(input("Enter your score: "))
    country = (input("Where are you living? "))
    student = {
        "name": name,
        "age": age,
        "country": country,
        "score": score
        }
    students.append(student)

show_students(students)
