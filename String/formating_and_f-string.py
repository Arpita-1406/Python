#Using .format() Method
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python
print("{name} is {age} years old".format(name="Bob", age=25))


#f-Strings (Formatted String Literals)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")