#1. Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case .
for i in range(1,8):
    match i:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thurdday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
                    
        



'''2. Write a program using match case that simulates a simple calculator.
    1. Ask the user for two numbers and an operation (+, -, *, /).
    2. Perform the operation using match case .'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operation = input("Enter operator:")

match operation:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)



















