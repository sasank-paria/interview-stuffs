'''
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.
'''
# The idea is based on the observation that to minimize the difference, 
# we must choose consecutive elements from a sorted packet. 
# first sort the array arr[0..n-1], then find the subarray of size m 
# with the minimum difference between the last and first elements.


arr=[7,3,2,4,9,12,56]

arr.sort()
m=3

min_diff = arr[-1] - arr[0]

    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
for i in range(0,len(arr)-m+1):
        min_diff = min(min_diff,arr[i+m-1]-arr[i])

print(min_diff)
