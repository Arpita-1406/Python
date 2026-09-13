#1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
n = int(input("Enter a number: "))

if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")


#2. Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for vote")
else:
    print("Sorry! You are not eligible for vote")


#3. Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.
n = int(input("Enter a number: "))

if n%2==0:
    print("Even")
else:
    print("Odd")


'''4. Take a student's marks and print:
80+ → A
60–79 → B
50–59 → C
Below 50 → Fail'''
n = int(input("Enter a number: "))

if n>80:
    print("A")
elif 60<=n<=79:
    print("B")
elif 50<=n<=59:
    print("C")
else:
    print("Fail")



'''5. Take salary and calculate:
Salary ≥ ₹50,000 → "High Salary"
Salary ≥ ₹25,000 → "Average Salary"
Below ₹25,000 → "Low Salary"'''
salary = float(input("Enter a number: "))

if salary>=50000:
    print("High salary")
elif salary>=25000:
    print("Average Salary")
else:
    print("Low Salary")


#6.Take revenue and cost and calculate profit/loss.
r = float(input("Enter a revenue: "))
c = float(input("Enter a cost: "))

profit = r-c
if profit >0:
    print("profit")
elif profit<0:
    print("Loss")
else:
    print("neither profit nor loss")
