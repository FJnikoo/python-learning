students = []
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

student = {
    "name": name,
    "age": age,
    "score": score
}
students.append(student)
print(students)
