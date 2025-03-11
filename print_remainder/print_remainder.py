#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

#Number Validator
def valid_num(msg):
    while True:#ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask user to quit            
def ask_quit():
    while True:#ask until valid input
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        #accept y/yes and n/no
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")
                          

try_again = True
while try_again:
    #Enter the divident and divisor
    num1 = valid_num("Enter Divident: ")
    num2 = valid_num("Enter Divisor:  ")
    
    #Divide and find the remainder
    remainder = num1 % num2
    
    #print remainder
    print(f"Remainder: {remainder}")
    
    #ask the user to quit 
    try_again = ask_quit()