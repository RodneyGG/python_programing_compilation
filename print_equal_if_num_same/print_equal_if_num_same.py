#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#Check if number is valid
def valid_num(msg):
    while True: #Ask until the user input a valid number
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input Two Numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")
#Check if two numbers are equal
if num1 == num2:
    #if equal print Equal
    print("Equal")