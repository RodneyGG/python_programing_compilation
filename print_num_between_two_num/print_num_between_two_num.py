#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#Ask the user to input two numbers
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
#Print the numbers between the two numbers
for num in range(num1 + 1, num2):
    print(num)
