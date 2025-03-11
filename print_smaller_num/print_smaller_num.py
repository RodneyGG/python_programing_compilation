#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

#Number Validator
def valid_num(msg):
    while True:
        num = input().strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")


#Input Two numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")

#Find the smaller number
if num1 > num2:
    #Print The smaller number
    print(num2)
else:
    #Print The smaller number
    print(num1)
    