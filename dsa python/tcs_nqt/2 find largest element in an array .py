# Example 1:
# Input:
#  arr[] = {2,5,1,3,0};
# Output:
#  5
# Explanation:
#  5 is the largest element in the array. 

def largest(arr) -> int :
    res = arr[0]

    for x in arr:
        res = max(res,x)
    return res

arr = [2,5,1,3,0,8]
print(largest(arr))