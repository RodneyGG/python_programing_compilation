#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

#ask user to quit
def ask_quit():
    while True:#ask until valid response
        ask_user = input("Do you want to print it again? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return True
        elif ask_user in ("n", "no"):
            return False
        else:
            print("Invalid Input")
    
try_again = True

while try_again:
    #print numbers from 0 to 100
    for i in range(0, 101):
        #if number does not end with 0
        if i % 10 != 0 and i != 0:
            #print number
            print(i)
            
    #ask the user to quit           
    try_again = ask_quit()

        