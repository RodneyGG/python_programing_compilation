"""
Prog02: Create a program that ask user to input 10 numbers. Display all numbers. 
For numbers with duplicate, display only the first entry.
"""

#Validate Number
def valid_num(msg):
    while True:#ask until valid inpu
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask user to quit
def ask_quit():
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else: 
            print("Invalid Input")

try_again = True
while try_again:
    #set
    numbers = set()

    #Ask user to input ten numbers
    for i in range(0,10):
        num = valid_num(f"Enter Number {i + 1}: ")
        #Add the number to the set
        numbers.add(num)

    #print the set
    print(numbers)
    
    try_again = ask_quit()