'''1. Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears'''
text = "  i love python programming  "

print(text.strip())

print(text.title())

print(text.count("o"))


#2. Check if the string "123abc" is alphanumeric.
text = "123abc"

print(text.isalnum())


#3. Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
text = "Coding in Python is fun"

print(text.replace("fun","awesome"))



#4. Find the index of the word "Python" in sentence.
text = "Coding in Python is fun"

print(text.index("Python"))



#5. Convert the entire sentence to uppercase and print it.
text = "Coding in Python is fun"

print(text.upper())