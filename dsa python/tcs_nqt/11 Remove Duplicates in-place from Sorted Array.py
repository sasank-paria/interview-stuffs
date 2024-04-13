# Example 1:
# Input:
#  arr[1,1,2,2,2,3,3]

# Output:
#  arr[1,2,3,_,_,_,_]


def func(arr):
    l,r = 0 , 1

    while r<len(arr):
        if arr[l] != arr[r]:
            arr[l+1] = arr[r]
            l+=1
        r+=1
    print(arr)

arr = [1,1,2,2,2,3,3]
func(arr)