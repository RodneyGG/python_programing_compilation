#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

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
    while True:
        ask_user = input("Do you wish to exit the program? (Y/N)").lower().strip()
        if ask_user in ("y","yes"):
            return False
        elif ask_user in ("n","no"):
            return True
        else:
            print("Invalid input") 

try_again = True

while try_again:
    #store the numbers in the list
    numbers = []

    #Ask the user to input ten numbers
    for i in range(0,10):
        number = valid_num(f"Input Number {i + 1}: ")
        numbers.append(number)
        
    #Make the first number the intial result and subtract it with the next numbers
    result = numbers[0]
    for num in numbers[1:]:
        result -= num 
    
    #Print Answer
    print(result)
    
    #ask user to quit
    try_again = ask_quit()