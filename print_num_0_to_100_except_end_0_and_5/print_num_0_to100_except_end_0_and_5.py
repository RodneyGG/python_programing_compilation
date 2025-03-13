#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#Ask user to quit
def ask_quit():
    while True: #Ask until valid response
        ask_user = input("Do you wish to see the numbers again? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return True
        elif ask_user in ('n', "no"):
            return False
        else:
            print("Invalid Input")
            
try_again = True

while try_again:
    #Print numbers from 0 to 100
    for i in range(0, 101):
        #Check if number end with 0 and 5
        if i % 10 != 0 and i % 5 != 0 and i != 0:
            #print number that not end in 5 and 0
            print(i) 
            
    #ask user to quit
    try_again = ask_quit()
   