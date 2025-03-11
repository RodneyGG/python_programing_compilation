"""
Prog02: Create a program that ask user to input 10 numbers. Display all numbers. 
For numbers with duplicate, display only the first entry.
"""

#Validate Number
def valid_num(msg):
    while True:#ask until valid inpu
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#set
numbers = set()

#Ask user to input ten numbers
for i in range(0,10):
    num = valid_num(f"Enter Number {i + 1}: ")
    #Add the number to the set
    numbers.add(num)

#print the set
print(numbers)