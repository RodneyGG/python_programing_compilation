#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#Number Validator
def valid_num(msg):
    while True:
        num = input(msg).strip()
        try:
            num = float(num)
            if num != int(num):
                print("This program does not accept numbers with decimal")
                continue
            return int(num)
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
    #Ask the user to input two numbers
    num1 = valid_num("Enter Number 1: ")
    num2 = valid_num("Enter Number 2: ")

    if num1 > num2:
        bigger_num = num1
        smaller_num = num2
    else:  
        bigger_num = num2
        smaller_num = num1
        
    #Print the numbers between the two numbers
    for num in range(smaller_num + 1, bigger_num):
        print(num)
    
    try_again = ask_quit()
