#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#Number validator
def valid_num(msg):
    while True:
        num = input(msg)
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")
    

#add a counter for odd
count = 0

#Ask the user to input ten numbers
for i in range(0,10):
    num = valid_num(f"Enter Number {i + 1}: ")
    #It will only accept whole numbers
    if num % 2 != 0 and num.is_integer():
        count += 1 #count the odd numbers
    
#print the number of odd count
print(count)