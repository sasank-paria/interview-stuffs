# Example 1:
# Input:
#  [1,2,4,7,7,5]
# Output:
#  Second Smallest : 2
# 	Second Largest : 5
# Explanation:
#  The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2


#sorting method will not work for duplicate values in an array
def func(arr):
    smallest = arr[0]
    largest = arr[0]

    for x in arr:
        smallest = min(smallest,x)
        largest = max(largest,x)
    
    secondsmall = largest
    secondlarge = smallest
    
    for y in range(len(arr)):
        if arr[y]<secondsmall and arr[y] != smallest :
            secondsmall = arr[y]

        if arr[y]>secondlarge and arr[y] != largest :
            secondlarge = arr[y] 

    print('second smallest:',secondsmall)
    print('second largest:',secondlarge)

arr = [1,2,4,7,7,5]
func(arr)