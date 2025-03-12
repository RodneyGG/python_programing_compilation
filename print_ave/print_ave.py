"""
Prog05: Create a program that ask user to input a number, 
continue asking until the user input is invalid. 
Display the average.
"""

#Handle Error
def handle_error(msg):
    num = input(msg).strip()
    try:
        return float(num)
    except ValueError:
        return None

#Variables
total = 0
count = 0

#Ask the user to input number, it will break once the user 
while True:
    num = handle_error("Enter Number: ")
    
    if num is None:
        break
    
    total += num
    count += 1


if count > 0:
    #Take the total value and divide it with the total number of entry
    average = total / count
    #display average
    print(average)
