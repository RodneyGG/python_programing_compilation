#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

#ask user to quit
def ask_quit():
    while True: #Ask until valid response
        ask_user = input("Do yo wish to show the odd numbers again? (Y/N)").lower().strip()
        if ask_user in ("y", "yes"):
            return True
        elif ask_user in ("n", "no"):
            return False
        else:
            print("Invalid Input")

try_again = True

while try_again:        
    #print 0 to 100 using while loop
    num = 0
    while num <= 100:
        #if number is odd print odd
        if num % 2 != 0:
            print(num)
        num += 1
        
    #ask user to quit
    try_again = ask_quit()
    