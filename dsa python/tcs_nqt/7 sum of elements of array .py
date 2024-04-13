
# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 15
# Explanation: Sum of all the elements is 1+2+3+4+5 = 15


def func(arr):
    res = 0
    for x in arr:
        res  = res + x 

    print(res)

arr = [1,2,3,4,5]
func(arr)