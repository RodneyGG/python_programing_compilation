"""
Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
"""
#Make a empty list called numbers
numbers = []

#Prompt the user to enter a number until an error is occured
while True:
    num = float(input("Enter Number: "))
    
    #print unique or duplicate
    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)

