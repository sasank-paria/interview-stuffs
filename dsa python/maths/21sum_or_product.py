'''
You are given a number ‘N’ and a query ‘Q.’ If ‘Q’ is 1,
 then you have to return the sum of all integers from 1 to ‘N,’ else if ‘Q’ is equal to 2 
 then you have to return the product of all integers from 1 to ‘N.’ 
'''

'''
Given N = 4 and Q = 1
Then the answer is 10 because the sum of all integers between 1 and 4 are
 1, 2, 3, and 4. Hence 1 + 2 + 3 + 4 is equal to 10.
'''

N = 4
Q = 2
sum = 0
prod = 1

if Q == 1 :
    for x in range(1,N+1):
        sum = sum + x
    print(sum)

if Q == 2 :
    for y in range(1,N+1):
        prod *= y
    print(prod)