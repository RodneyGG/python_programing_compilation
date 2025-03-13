#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Number Validator
def valid_num(msg):
    while True: #Ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#ask user to quit
def ask_quit():
    while True:#ask until valid response
        ask_user = input("Do you wish to exit the program? (Y/N)").strip().lower()
        if ask_user in ("y", "yes"):
            return False
        elif ask_user in ("n", "no"):
            return True
        else:
            print("Invalid Input")

#Add a list to append the numbers
numbers = []
try_again = True

while try_again:
    #Ask user to input Ten numbers
    for i in range(0, 10):
        num = valid_num(f"Enter Number {i + 1}: ")
        numbers.append(num)

    #Add ten numbers and print the result
    print(sum(numbers))
    
    #ask the user to quit
    try_again = ask_quit()