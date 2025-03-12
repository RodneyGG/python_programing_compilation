"""
Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. 
Display the number with the most number of duplicate.
"""

#handle error
def handle_error(msg):
    num  = input(msg)
    try:
        return float(num)
    except ValueError:
        return None

#make a dictionary
count_numbers = {}
numbers = []

#Ask user to input a number until an error has occured
while True:
    number = handle_error("Enter a Number: ")
    
    if number is None:
        break
    
    numbers.append(number)
    
    #add to the dictionary
    for num in numbers:
        count_numbers[num] = count_numbers.get(num, 0) + 1
        
    

if count_numbers:
    #Find the number with the most duplicate
    most_duplicate = max(count_numbers, key=count_numbers.get)
    #print the number
    print(most_duplicate)
