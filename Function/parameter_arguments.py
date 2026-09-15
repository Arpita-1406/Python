def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8


def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!


def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")