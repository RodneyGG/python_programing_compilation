#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

#Check if valid Number 
def valid_num(msg):
    while True: #Ask until user give a valid response 
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#Input Two numbers
num1 = valid_num("Enter Number 1: ")
num2 = valid_num("Enter Number 2: ")
#Add the number
sum = num1 + num2
#print the sum
print(sum) 