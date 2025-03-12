"""
Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
"""
#Number Validator
def valid_num(msg):
    while True: #ask until valid response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")


#Make a list and set
numbers = []
duplicate_numbers = set()

#ask user to print ten numbers
for i in range(0,10):
    num = valid_num(f"Enter a number {i + 1}: ")
    #Append all numbers in the list
    if num in numbers:
    #if number already in the list add to the set
        duplicate_numbers.add(num)
    #add every number to the list
    numbers.append(num)
    
#print the set
print(duplicate_numbers)