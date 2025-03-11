#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

#Ask user to quit
def ask_quit():
    while True:#ask until valid input
        ask_user = input("Do you wish to show the even number again? (Y/N)").lower().strip()
        #accepts y/yes and n/no
        if ask_user in ("y", "yes"):
            return True
        elif ask_user in ("n", "no"):
            return False
        else:
            print("Invalid Input")

try_again = True

while try_again:
    #Print 0 to 100
    for i in range(0,101):
    #Check if the number is even
        if i % 2 == 0 and i != 0:
            #print only even
            print(i)
    #ask user to quit
    try_again = ask_quit()