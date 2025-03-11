"""
Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
"""

def handle_error(msg):
    while True:
        num = input(msg)
        try:
            return float(num)
        except ValueError:
            return None

#Make a empty list called numbers
numbers = []

#Prompt the user to enter a number until an error is occured
while True:
    num = handle_error("Enter Number: ")
    
    if num is None:
        break
    #print unique or duplicate
    elif num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)

