#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

#Check Valid Number
def valid_num(msg):
    while True:#ask until valid input
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")
        
#Input Two Numbers
num1 = valid_num("Enter Number: ")
num2 = valid_num("Enter Exponent: ")

#Make the formula num1^num2
answer = num1 ** num2

#print answer
print(answer)