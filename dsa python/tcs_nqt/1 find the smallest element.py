# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 0
# Explanation: 0 is the smallest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 5
# Explanation: 5 is the smallest element in the array.

def small(arr):

    res = arr[0]
    for x in arr:
        res = min(x,res)
    return res

print(small([2,5,1,3,0]))
print(small([8,10,5,7,9]))