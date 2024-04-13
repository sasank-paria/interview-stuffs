# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5} K=2
# Output: {3,4,5,1,2}
# Explanation: Rotate the array to right by 2 elements.

# Example 2:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
# Output: {4,5,6,7,1,2,3}
# Explanation: Rotate the array to right by 3 elements.


def func(arr,k):

    for x in range(k):
        arr.append(arr[x])
    
    for x in range(k):
        arr.pop(0)   # 0 is index no.
    print(arr)

arr = [1,2,3,4,5]
k = 2
func(arr,k)