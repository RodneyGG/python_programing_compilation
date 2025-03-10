#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

#Check if valid number
def valid_num(msg):
    while True: #Ask Until user give a valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask the user to quit            
def ask_quit():
    while True:#ask until valid input
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        #accept y/yes or n/no
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input. Only Enter Y/N")

try_again = True
while try_again:
    #Input two number
    num1 = valid_num("Enter Number 1: ")
    num2 = valid_num("Enter Number 2: ")
    
    #Find the product
    product = num1 * num2
    
    #print the product
    print(product)
    
    #Ask the user to quit
    try_again = ask_quit()