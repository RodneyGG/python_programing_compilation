"""
Prog03: Create a program that ask user to input a number, 
continue asking until the user input is invalid. 
Display the highest number
"""
#Handle error
def handle_error(msg):
    num = input(msg)
    try:
        return float(num)
    except ValueError:
        return None

#make a list called numbers
numbers = []
#ask user to input number until error has occured
while True:
    num = handle_error("Enter Number: ")
    
    if num is None:
        break
    
    numbers.append(num)

 
if numbers:
    #find the highest number
    highest_num = max(numbers)
    #print the number
    print(highest_num)