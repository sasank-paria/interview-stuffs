'''
Given N, count all ‘a’ and ‘b’ that satisfy the condition a^3 + b^3 = N. 
Examples: 

Input : N = 9
Output : 2
1^3 + 2^3 = 9
2^3 + 1^3 = 9

Input : N = 28
Output : 2
 1^3 + 3^3 = 28
 3^3 + 1^3 = 28
'''

N = 9
temp = 0
for x in range(1,N+1):
    for y in range(x+1,N+1):
        if x**3 + y**3 == N :
            temp = temp +2
        else :
            temp = temp+1

print(temp)