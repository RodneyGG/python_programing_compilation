#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

#Check Valid Number
def valid_num(msg):
    while True:#ask until valid input
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")
        
#ask user to quit
def ask_quit():
    while True:
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
    #Input Two Numbers
    num1 = valid_num("Enter Number: ")
    num2 = valid_num("Enter Exponent: ")

    #Make the formula num1^num2
    answer = num1 ** num2

    #print answer
    print(answer)
    
    try_again = ask_quit()