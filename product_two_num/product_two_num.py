#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

#Check if valid number
def valid_num(msg):
    while True: #Ask Until user give a valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input two number
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")
#Find the product
product = num1 * num2
#print the product
print(product)