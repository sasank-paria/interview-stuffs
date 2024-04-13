# Example 1:
# Input: [2,4,1,3,5] = [1 2 3 4 5]
# Output: 3

# Example 2:
# Input: [2,5,1,7] = [1 2 5 7]
# Output: 3.5

# What is a Median?
# Median is defined as the value which is present in the middle for a series of values. 
# Note, in order to find the median of an array of integers, we must make sure they are sorted.

def func(arr):
    arr.sort()
    median = 0

    #even length
    if len(arr)%2 == 0 :
        first = len(arr)//2
        second= (len(arr)//2) - 1
        median = (arr[first] + arr[second]) / 2
        print(median)
    
    if len(arr)%2 != 0 :
        median = arr[len(arr)//2]
        print(median)

arr = [2,4,1,3,5] 
arr2 =  [2,5,1,7]
func(arr2)