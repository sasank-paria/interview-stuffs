'''
Input: arr[] = {1, 2, 3}, L = 2, R = 8
Output: 14
Explanation:
The array, arr[] after concatenation is {1, 2, 3, 1, 2, 3, 1, 2, …} 
and the sum of elements from index 2 to 8 is 2 + 3 + 1 + 2 + 3 + 1 + 2 = 14.
'''

arr = [1,2,3]
L=2
R=8
addition = 0

x = 0

for x in range(0,R+1):
    arr.append(arr[x])
print(arr)

for y in range(L-1,R):
    addition = addition + arr[y]

print(addition)