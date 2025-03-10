#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

#Check if number is valid
def valid_num(msg):
    while True:#Ask until valid input
        num = input(msg)
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input Two Numbers
num1 = valid_num("Enter Dividend: ")
num2 = valid_num("Enter Divisor:  ")

#Divide Two Numbers
quotient = num1 / num2

#Print the quotient
print(quotient)