#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#Number Validator
def valid_num(msg):
    while True: #Ask Until Valid Response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")
            
#ask user to quit
def ask_quit():
    while True: #Ask until valid response
        ask_user = input("Do yo wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

try_again = True

while try_again: 
    #add a counter
    count = 0

    #Ask the user to input ten numbers
    for i in range(0,10):
        num = valid_num(f"Enter Number {i + 1}: ")
        #count even numbers
        if num % 2 == 0 and num.is_integer():
            count += 1

    #print count of even
    print(count)
    
    #ask user to quit
    try_again = ask_quit()
    