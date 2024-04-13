# Example 2:
# Input:  N=6, array[] = {1,2,1,1,5,1}
# Output: 1.8

def func(arr):
    average = 0
    add = 0
    res= 0
    for x in arr:
        add = add+x
    average = add/len(arr)
    res= round(average,1)  #IMP   this will round of to 1 decimal value 1.8333333 will become 1.8
    print(res)

arr = [1,2,1,1,5,1]
func(arr)