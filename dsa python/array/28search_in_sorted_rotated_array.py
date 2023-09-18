'''
Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
Output : Not found
'''

nums =[5,6,7,8,9,10,1,2,3]
target = 3

for x in range(len(nums)):
    if nums[x]==target:
        print(x)