#1. Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
def increment():
    counter = 0
    counter += 1
    print(counter)

increment()
increment()
increment()
increment()



#2. Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a,b):
    '''

    Multiply two numbers.

    parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    '''
    return a * b

# Example usage
print(multiply(5,3)) #15
print(multiply(2.5, 4)) #10.0
help(multiply)