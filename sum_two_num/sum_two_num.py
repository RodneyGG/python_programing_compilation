#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

#Check if valid Number 
def valid_num(msg):
    while True: #Ask until user give a valid response 
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask the user to quit
def ask_quit():
    while True:
        ask_user = input("Do you want to quit the program? (Y/N)").lower().strip()
        if ask_user in ("y","yes"):
            return False
        elif ask_user in ("n","no"):
            return True
        else:
            print("Invalid Input. Only Enter Y/N")
            
try_again = True

while try_again:
    #Input Two numbers
    num1 = valid_num("Enter Number 1: ")
    num2 = valid_num("Enter Number 2: ")
    #Add the number
    sum = num1 + num2
    #print the sum
    print(sum) 
    
    #ask the user to quit 
    try_again = ask_quit()