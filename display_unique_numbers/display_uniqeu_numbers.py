"""
Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
"""
#List of numbers
numbers = []
unique_numbers = []

#Ask the user to input 10 numbers
for i in range(0,10):
    number = float(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

#Check the number that has no duplicate
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

#Print numbers that has no dubplicates
print(unique_numbers)

