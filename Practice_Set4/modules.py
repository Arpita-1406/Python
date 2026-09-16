'''1. Import the math module and use it to:
Find the square root of 144
Calculate sin(90°) (hint: use math.radians())'''
import math

a = math.sqrt(144)
b = math.sin(math.radians(90))
print(a, b)


#2. Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
import requests # pip install requests

a = requests.get("https://api.github.com/")
print(a.json())


#3. Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
# main.py


from my_utils import is_even

# Example usage
print(is_even(4))   # True
print(is_even(7))   # False
