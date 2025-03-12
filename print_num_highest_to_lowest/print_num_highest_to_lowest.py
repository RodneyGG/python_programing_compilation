"""
Prog04: Create a program that ask user to input a number, 
continue asking until the user input is invalid. 
Display the number from highest to lowest. 
Clue: sort() function
"""
#make a list called numbers
numbers = []
#Ask user to input numbers until error occure
while True:
    num = float(input("Enter Number: "))
    numbers.append(num) 
#Sort highest to lowest
#print sorted values