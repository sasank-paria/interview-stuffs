# Armstrong number is a number that is equal to the sum of cubes of its digits. 

# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

number = (input("enter a number:\n"))
armstrong = 0

for n in number:
    n=int(n)
    armstrong = armstrong + n**3   # if the number is greater than 3 digits then it should be raised to number of digits.

number = int(number)

if armstrong == number :
    print('it is a armstrong number')

else:
    print('it is not a armstrong number')