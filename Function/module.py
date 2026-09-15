# Two types of modules in Python: 
# - Built in Modules 
# - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
import math 
import requests

print(math.sqrt(16))

r = requests.get("https://www.google.com")
print(r.text)



print(math.sqrt(16))  # Output: 4.0


response = requests.get("https://api.github.com")
print(response.status_code)