#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

#Print 0 to 100
for i in range(0,101):
#Check if the number is even
    if i % 2 == 0 and i != 0:
        #print only even
        print(i)