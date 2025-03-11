#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#Print numbers from 0 to 100
for i in range(0,101):
    #Check if number end with 0 and 5
    if i % 10 != 0 and i % 5 != 0 and i != 0:
        #print number that not end in 5 and 0
        print(i) 
   