# For example, factorial of 5 is 5 * 4 * 3 * 2 * 1 which equals to 120

number = int(input('enter a number: \n'))
factorial = 1

while number is not 0:
    factorial = factorial * number
    number=number-1

print(factorial)