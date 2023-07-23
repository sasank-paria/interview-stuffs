
#by for loop  #boring way

num1 = 5874
num2=str(num1)

for x in num2:
    print(x)

#----------------------------------------

num1 = 3243

num2 = [int(i) for i in str(num1)]
print(num2)

#-----------------------------------------

int = 389

digit1 = int%10

print(digit1)

num2 = int//10

digit2 = num2%10
print(digit2)

num3 = num2 // 10

digit3 = num3%10

print(digit3)