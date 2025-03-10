#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

#check if number is valid
def valid_num(msg):
    while True: #Ask until the user give a valid number
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input Two Numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")

#Find the bigger number
if num1 > num2:
    #print the bigger number
    print(num1)
else: 
    #print the bigger number
    print(num2)