"""
Prog04: Create a program that ask user to input a number, 
continue asking until the user input is invalid. 
Display the number from highest to lowest. 
Clue: sort() function
"""
#Handle Errors
def handle_error(msg):
    num = input(msg)
    try:
        return float(num)
    except ValueError:
        return None

#make a list called numbers
numbers = []
#Ask user to input numbers until error occure
while True:
    num = handle_error("Enter Number: ")
    
    if num is None:
        break
    
    numbers.append(num)
if numbers: 
    #Sort highest to lowest
    numbers.sort(reverse=True)
    #print sorted values
    print(numbers)