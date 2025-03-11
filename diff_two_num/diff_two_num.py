#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

#Add a number validator
def valid_num(msg):
    while True: #Ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask user to quit
def ask_quit():
    while True:#Ask Until Valid Response
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
    num1 = valid_num("Enter Number: ")
    num2 = valid_num("Enter Number: ")
    
    #find the diference of two numbers
    answer = num1 - num2
    
    #Print Answer
    print(f"{num1} - {num2} = {answer}")
    
    #ask user to quit
    try_again = ask_quit()