"""
Prog05: Create a program that ask user to input a number, 
continue asking until the user input is invalid. 
Display the average.
"""

#Variables
total = 0
count = 0

#Ask the user to input number, it will break once the user 
while True:
    num = float(input("Enter Number"))
    total += num
    count += 1
    
    #Take the total value and divide it with the total number of entry
    average = total / count
    #display average
    print(average)
