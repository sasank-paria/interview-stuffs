# The Fibonacci numbers are the numbers in the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..


number = int(input('enter a number:'))

n1 = 0
n2 = 1

print(n1)
print(n2)

while number is not 0 :
    n3 = n1 + n2
    n1= n2
    n2 = n3                 
    print(n2)
    number=number-1