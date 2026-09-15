'''1. Create a string variable name with your full name. Print:
The first character
The last character
The length of the string'''
name = "Arpita"

print(name[0])
print(name[-1])
print(len(name))


#2. Concatenate two strings: "Hello" and "World" with a space in between.
str1 = "Hello"
str2 = "world"

print(str1,str2)


#3. Write a program that counts how many vowels are in a given string.
text = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in text.lower():
    if(char in vowels):
        sum += 1

print(f"there are {sum} vowels in this text")


#4. Take a user input string and check if it is a palindrome (same forwards and backwards).
text = input("Enter a string: ")

if(text == text[::-1]):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")