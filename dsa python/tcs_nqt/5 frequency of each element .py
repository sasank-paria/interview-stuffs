# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	      5  2
#         15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array

from collections import Counter

def func(arr):
    occur = Counter(arr)
    for x , y in zip(occur.keys(), occur.values()):
        print(x,y)

arr = [10,5,10,15,10,5]
func(arr)