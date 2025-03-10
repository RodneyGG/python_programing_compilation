#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#Check if number is valid
def valid_num(msg):
    while True: #Ask until the user input a valid number
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#To quit the program           
def ask_again():
    while True: #Ask the user until valid response
        ask_user =  input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input. Only Enter Y/N")

try_again = True
while try_again():    
    #Input Two Numbers
    num1 = valid_num("Enter Number 1: ")
    num2 = valid_num("Enter Number 2: ")
    #Check if two numbers are equal
    if num1 == num2:
        #if equal print Equal
        print("Equal")
    
    #ask the user to quit
    try_again = ask_again()