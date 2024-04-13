
# Example 1:
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first 
# element will occupy the fifth position, the second element occupies the fourth position and so on.

#shortcut method
def reverse(arr,n):
    arr[::-1]
    print(arr)


#alternate method
def reverse2(arr,n):
    p1,p2 = 0 , n-1 

    while p1 < p2 :
        arr[p1] , arr[p2] = arr[p2] , arr[p1]
        p1+=1
        p2-=1
    print(arr)


n= 5
arr = [5,4,3,2,1]
reverse2(arr,n)