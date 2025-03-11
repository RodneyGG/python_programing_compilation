#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

#Number Validator
def valid_num(msg):
    while True:#Ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input Two numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")

#Check if num is the not the same
if num1 != num2: 
    #if number is not the same print "Not Equal"
    print("Not Equal")