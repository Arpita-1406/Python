#1. Write a recursive function factorial(n) that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

print(factorial(4))


#2. Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
   if n == 0:
      return 0
   return n%10 + sum_of_digits(n//10)
print(sum_of_digits(7532))


#3. Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
   
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    for i in range(n):
        print(fib(i), end=" ")

# Example usage
fibonacci(10)   # Prints: 0 1 1 2 3 5 8 13 21 34
