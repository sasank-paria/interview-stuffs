'''69

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''

x = 8

n=1
multiply = 0

if x == 0:
    return 0

if x == 1:
    return 1

while n <= x:
    multiply = n*n
    if multiply>x:
        print(n-1)
        break
    n+=1

