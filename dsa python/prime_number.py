# The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.

number=int(input('enter a number'))

if number==1:
    print('it is not a prime number')

if number == 2:
    print("it is a prime number")
    
if number % 2 == 0:
    print("it is not a prime number")

else: 
    for x in range(3,number):
        if number%x==0:
            print ("It' not a Prime Number.")
            break
        else:
           print ('A Prime.') 
           break
        