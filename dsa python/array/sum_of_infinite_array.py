'''
Input: arr[] = {1, 2, 3}, L = 2, R = 8
Output: 14
Explanation:
The array, arr[] after concatenation is {1, 2, 3, 1, 2, 3, 1, 2, …} 
and the sum of elements from index 2 to 8 is 2 + 3 + 1 + 2 + 3 + 1 + 2 = 14.
'''

arr = [5,2,6,9]
L=10
R=13
addition = 0

x = 0
while x<R:
    for x in range(0,len(arr)+1):
        arr.append(arr[x])
    x=x+1

for y in range(L,R+1):
    addition = addition + arr[y]

print(addition)