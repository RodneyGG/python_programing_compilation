#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#add a counter
count = 0

#Ask the user to input ten numbers
for i in range(0,10):
    num = float(input(f"Enter Number {i + 1}"))
    #count even numbers
    if num % 2 == 0 and num.is_integer():
        count += 1

#print count of even
print(count)