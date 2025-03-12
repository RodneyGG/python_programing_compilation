"""
Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
"""

def handle_error(msg):
    while True:
        num = input(msg)
        try:
            return float(num)
        except ValueError:
            if numbers:
                print(lowest_num)
            else:
                break

#Make a list to store the numbers
numbers = []



#Ask user to input a number until error has occured
while True:
    num = handle_error("Enter a Number: ")
    #append numbers to the list 
    numbers.append(num)
    #identify which is the smaller number
    lowest_num = min(numbers)
    
    
    
   



