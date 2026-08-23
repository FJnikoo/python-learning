name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
score = int(input("Enter your score: "))

student = {
    "name": name,
    "age": age,
    "country": country,
    "score": score
}

def show_student(student):
    name = student["name"].capitalize()
    age = student["age"]
    country = student["country"]

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")

def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

show_student(student)
result = check_score(student["score"])
print(f"Your result is: {result}")       
