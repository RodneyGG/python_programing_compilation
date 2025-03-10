#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

#check if number is valid
def valid_num(msg):
    while True: #Ask until the user give a valid number
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Ask the user if it want to continue            
def ask_retry():
    while True: # ask until the user give a valid input
        #remove the leading and trailing spaces and lower the character
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        #accept yes/y and no/n
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")
            
try_again = True

while try_again:
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
        
    try_again = ask_retry()