#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

#Number Validator
def valid_num(msg):
    while True: #Ask until Valid Response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask user to quit
def ask_quit():
    while True: #Ask until valid response
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else: 
            print("Invalid Input")
            
try_again = True

while try_again:
    #Ask the user to input two numbers
    dividend = valid_num("Enter Dividend: ")
    divisor = valid_num("Enter Divisor: ")

    #Find the quotient without the decimal(floor division)
    quotient = int(dividend // divisor)

    #Print the quotient
    print(quotient)
    
    try_again = ask_quit()