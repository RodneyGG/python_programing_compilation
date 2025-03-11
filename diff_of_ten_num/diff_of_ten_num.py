#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

#store the numbers in the list
numbers = []

#Ask the user to input ten numbers
for i in range(0,10):
    number = float(input(f"Input Number {i + 1}: "))
    numbers.append(number)
    
#Make the first number the intial result and subtract it with the next numbers
result = numbers[0]
for num in numbers[1:]:
    result -= num 
#Print Answer
print(result)