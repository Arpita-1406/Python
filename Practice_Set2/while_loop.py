#1. Print numbers from 1 to 10 using a while loop.
i =1
while i<=10:
    print(i)
    i+=1


#2. Write a program that keeps asking the user to enter a password until they enter the correct one.
password = "xcv2345b6"
enter_pass = input("Enter Password: ")

while (enter_pass != password):
    enter_pass = input("Wrong Password! Try again and enter password: ")

print("Success! You are logged in")



#3. Use a while loop to reverse a given number (e.g., 123 → 321).
num = 45222

print(int(str(num)[::-1]))


#4. Print 'MBA Finance' 5 times.
i=1
while i<=5:
    print("MBA Finance")
    i+=1


#5. Find the total of sales [500, 700, 900].
sales = [500, 700, 900]
total =0
for amount in sales:
    total+= amount
    print(total)


