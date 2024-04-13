# Example 1:
# Input: 8 7 1 6 5 9
# Output: 1 5 6 9 8 7
# Explanation: First three elements are in the ascending order and next three elements are in the descending order.


def func(arr):
    half = len(arr)//2  #half = 3
    arr.sort() 
    res=arr[0:half]
    
    #decreasing order appending
    for x in range(len(arr)-1,half-1,-1):  #(start,stop,step)
        print('index',x)
        res.append(arr[x])

    print(res)


arr = [8, 7, 1, 6, 5, 9]
func(arr)
