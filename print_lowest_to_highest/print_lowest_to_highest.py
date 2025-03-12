"""
Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. 
Display the number from lowest to highest. Clue: sort() function
"""
#handle errors
def handle_error(msg):
    num = input(msg).strip()
    try: 
        return float(num)
    except ValueError:
        return None

#make a list called numbers
numbers = []

#Ask the user to input a number until error has occured
while True:
    num = handle_error("Enter Number: ")
    
    if num is None:
        break
    
    #Append number to the list
    numbers.append(num)

if numbers:
    #sort the numbers
    numbers.sort()
    #print the sorted numbers
    print(numbers)
