"""
Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
"""

def handle_error(msg):
    while True:
        num = input(msg)
        try:
            return float(num)
        except ValueError:
            return None

#Make a list to store the numbers
numbers = []

#Ask user to input a number until error has occured
while True:
    num = handle_error("Enter a Number: ")
    
    if num is None:#If num is a blank it will break
        break
    
    #append numbers to the list 
    numbers.append(num)
    

if numbers:
    #identify which is the smaller number
    lowest_num = min(numbers)
    print(lowest_num)
else:
    print("No Valid Numbers Entered")    
    
    
    
   



