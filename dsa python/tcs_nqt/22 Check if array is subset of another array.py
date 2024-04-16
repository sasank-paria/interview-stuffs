# Example 1:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [2,4,3,1,7,5,15]
# Output: arr1[] is a subset of arr2[]

# Example 2:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [4,5,2]
# Output: arr1[] is not a subset of arr2[]

# Example 3:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [11,12,13,15,16]
# Output: arr1[] is not a subset of arr2[]


def func(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    res = set1.issubset(set2)
    print(res)

arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]
func(arr1,arr2)
