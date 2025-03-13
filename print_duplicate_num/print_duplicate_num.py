"""
Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
"""
#Number Validator
def valid_num(msg):
    while True: #ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Ask the user to quit
def ask_quit():
    while True: #ask until valid response
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")


#Make a list and set
numbers = []
duplicate_numbers = set()

try_again = True

while try_again:
    #ask user to print ten numbers
    for i in range(0, 10):
        num = valid_num(f"Enter a number {i + 1}: ")
        #Append all numbers in the list
        if num in numbers:
        #if number already in the list add to the set
            duplicate_numbers.add(num)
        #add every number to the list
        numbers.append(num)
        
    #print the set
    print(duplicate_numbers)
    
    try_again = ask_quit()