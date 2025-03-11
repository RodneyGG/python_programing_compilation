#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

#Number Validator
def valid_num(msg):
    while True:
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Enter the divident and divisor
num1 = valid_num("Enter Divident: ")
num2 = valid_num("Enter Divisor:  ")
#Divide and find the remainder
remainder = num1 % num2
#print remainder
print(remainder)