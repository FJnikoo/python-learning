person = {
    "name": "Alice",
    "age": 30,
    "country": "USA"
}

def introduce(person):
    name = person["name"].capitalize()
    age = person["age"]
    country = person["country"]
    print(f"Hello, {name}!")
    print(f"You are {age} years old")
    print(f"You live in {country}")

introduce(person)
