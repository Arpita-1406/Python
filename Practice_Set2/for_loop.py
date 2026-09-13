#1. Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)


#2. Print the multiplication table of a number (entered by user).
n = int(input("Enter a number: "))

for i in range(1,11):
    print(n,"x", i,"=", n*i)



#3. Calculate the sum of all numbers from 1 to 100 using a for loop.
sum =0
for i in range(1, 101):
    sum += i
    print( sum)


'''4. Print the following pattern using a for loop:
*
**
***
****'''
for i in range(1,5):
    print("*"*i)


#5.Print even numbers from 2 to 20.
for i in range(1,21):#solution1
    if i%2==0:
        print(i)

for i in range(2,21,2):#solution2
    print(i)


#6.Print numbers from 10 down to 1.
for i in range(10,0,-1):
    print(i)


#7.Print the multiplication table of 5.
for i in range(1,11):
    print("5 x", i,"=", 5*i)
