#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

#Number Validator
def valid_num(msg):
    while True: #Ask until Valid Response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Ask the user to input two numbers
dividend = valid_num("Enter Dividend: ")
divisor = valid_num("Enter Divisor: ")

#Find the quotient without the decimal(floor division)
quotient = int(dividend // divisor)

#Print the quotient
print(quotient)