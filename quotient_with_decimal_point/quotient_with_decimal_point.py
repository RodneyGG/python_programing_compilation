#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

#Check if number is valid
def valid_num(msg):
    while True:#Ask until valid input
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask the user to quit
def ask_quit():
    while True:#ask until valid input
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        #accept y/yes and n/no
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input. Type only Y/N")

try_again = True
while try_again:
    #Input Two Numbers
    num1 = valid_num("Enter Dividend: ")
    num2 = valid_num("Enter Divisor:  ")

    #Divide Two Numbers
    quotient = num1 / num2

    #Print the quotient
    print(quotient)
    
    #ask user to quit
    try_again = ask_quit()