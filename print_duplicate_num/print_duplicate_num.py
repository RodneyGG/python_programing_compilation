"""
Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
"""
#Make a list and set
numbers = []
duplicate_numbers = set()

#ask user to print ten numbers
for i in range(0,10):
    num = float(input(f"Enter a number {i + 1}: "))
    #Append all numbers in the list
    if num in numbers:
    #if number already in the list add to the set
        duplicate_numbers.add(num)
    #add every number to the list
    numbers.append(num)
    
#print the set
print(duplicate_numbers)