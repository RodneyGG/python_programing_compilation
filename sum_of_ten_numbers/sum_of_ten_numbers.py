#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Add a list to append the numbers
numbers = []

#Ask user to input Ten numbers
for i in range(0,10):
    num = float(input(f"Enter Number {i + 1}: "))
    numbers.append(num)

#Add ten numbers and print the result
print(sum(numbers))