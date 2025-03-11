#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

#Number Validator
def valid_num(msg):
    while True:#Ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask the user to quit
def ask_quit():
    while True:#Ask until valid response
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        #accepts y/yes and n/no
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

try_again = True
while try_again:
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
    
    #ask user to quit
    try_again = ask_quit()