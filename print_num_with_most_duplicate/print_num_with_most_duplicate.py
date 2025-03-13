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


#Ask user to input a number until an error has occured
while True:
    number = handle_error("Enter a Number: ")
    
    if number is None:
        break
    
    
    #add to the dictionary
    count_numbers[number] = count_numbers.get(number, 0) + 1
        
    

if count_numbers:
    #find the most duplicate number
    highest_count = max(count_numbers.values())
    
    most_duplicate = []
    
    #Find the number with the most duplicate
    for num, count in count_numbers.items():
        if count == highest_count:
            most_duplicate.append(num)
    
    #print the number
    print(most_duplicate)
