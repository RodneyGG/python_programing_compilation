"""
Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
"""
#number validator
def valid_num(msg):
    while True:#ask until valid inpu
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#List of numbers
numbers = []
unique_numbers = []

#Ask the user to input 10 numbers
for i in range(0,10):
    number = valid_num(f"Enter Number {i + 1}: ")
    numbers.append(number)

#Check the number that has no duplicate
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

#Print numbers that has no dubplicates
print(unique_numbers)

