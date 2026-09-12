#Q1. Create variables and take input :
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
City = input("Enter your city: ")
Course = input("Enter your Course: ")

print(Name)
print(Age)
print(City)
print(Course)


#Q2. Take two numbers from the user and print their sum.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
sum = num1 + num2 
print("Sum of two numbers: ", sum)

#Q3. Take: Total marks,  Obtained marks and calculate percentage.
Total_marks = float(input("Enter total marks: "))
Obtained_marks = float(input("Enter your marks: "))
percentage = Obtained_marks/Total_marks*100

print("percentage: ", percentage )

#Q4. Take the price of a product and quantity, then calculate the total amount.
price = float(input("Enter price of a product: "))
quantity = float(input("Enter quantity of a product: "))
total_amount = price*quantity

print("Total amount: ", total_amount)