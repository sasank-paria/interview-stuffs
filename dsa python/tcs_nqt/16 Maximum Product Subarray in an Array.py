# Example 1:
# Input:

#  Nums = [1,2,3,4,5,0]
# Output:

#  120
# Explanation:

#  In the given array, we can see 1×2×3×4×5 gives maximum product value.


def func(arr):
    res = 0
    for x in range(len(arr)):
        mult = 1
        for y in range(x,len(arr)):
            mult = mult *arr[y]
            res = max(res,mult)
    print(res)

arr = [1,2,3,4,5,0]
arr2 = [1,2,-3,0,-4,-5]
func(arr2)