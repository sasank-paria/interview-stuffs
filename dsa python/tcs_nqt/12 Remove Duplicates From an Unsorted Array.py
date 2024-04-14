# Example 1:
# Input: arr[]={2,3,1,9,3,1,3,9}
# Output:  {2,3,1,9}

from collections import Counter
def func(arr):
    map = Counter(arr)
    res = []

    for x in map.keys() :
        res.append(x)
    print(res)

arr = [2,3,1,9,3,1,3,9]
func(arr)