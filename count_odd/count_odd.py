#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#add a counter for odd
count = 0

#Ask the user to input ten numbers
for i in range(0,10):
    num = float(input(f"Enter Number {i + 1}: "))
    if num % 2 != 0:
        count += 1 #count the odd numbers
    
#print the number of odd count
print(count)