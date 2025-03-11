#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#Number Validator
def valid_num(msg):
    while True:
        num = input(msg).strip()
        try:
            num = float(num)
            if num != int(num):
                print("This program does not accept numbers with decimal")
                continue
            return int(num)
        except ValueError:
            print("Invalid Input")
        
#Ask the user to input two numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")

if num1 > num2:
    bigger_num = num1
    smaller_num = num2
else:  
    bigger_num = num2
    smaller_num = num1
    
#Print the numbers between the two numbers
for num in range(smaller_num + 1, bigger_num):
    print(num)
