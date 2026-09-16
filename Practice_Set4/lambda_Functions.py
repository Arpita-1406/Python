#1. Write a lambda function that adds two numbers and test it.
add = lambda a, b: a + b

print(add(3, 5))


#2. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares
square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]

print(list(map(square, list1)))