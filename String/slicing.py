text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)


text = "Python Programming"
print(text[::2])   # Output: Pto rgamn
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)


text = "Welcome to Python!"
print(text[:7])   # Output: Welcome
print(text[-7:])  # Output: Python!
print(text[3:-3]) # Output: come to Pyt