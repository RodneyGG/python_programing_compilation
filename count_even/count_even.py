#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#Number Validator
def valid_num(msg):
    while True: #Ask Until Valid Response
        num = input(msg).strip()
        try:
            return float(num)
        except ValueError:
            print("Invalid Input")

#add a counter
count = 0

#Ask the user to input ten numbers
for i in range(0,10):
    num = valid_num(f"Enter Number {i + 1}")
    #count even numbers
    if num % 2 == 0 and num.is_integer():
        count += 1

#print count of even
print(count)