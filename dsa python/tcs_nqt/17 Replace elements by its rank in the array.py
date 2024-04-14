# Example 1:
# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…



def func(arr):
    original = arr.copy()
    arr.sort()
    res = []

    for x in original:
        res.append((arr.index(x)) + 1)
    print(res)


arr = [20 ,15, 26, 2, 98, 6]
func(arr)
