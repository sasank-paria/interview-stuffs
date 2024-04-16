# Example 2:
# Input: array[]={6,7,9,5,3,10} k=10
# Output: 5
# Explanation: The answer is 5 because 10 is present at 5th index.


def func(arr,k):

    for x in range(len(arr)):
        if arr[x] == k:
            print(x)

arr = [6,7,9,5,3,10]
k = 10
func(arr,k)
    
