'''
input: 1 1 2
output: 1
because 1 is repeated
'''

from collections import Counter

arr = [1,3,4,2,2]
arr = [1,1,2]

for x in range(0,len(arr)-1):
    for y in range(x+1,len(arr)):
        if arr[x]==arr[y]:
             print(arr[y])