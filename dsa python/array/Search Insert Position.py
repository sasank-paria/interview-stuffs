'''35

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

def searchInsert(self, nums: List[int], target: int) -> int:
    for x in range(len(nums)):
        if(nums[x]==target):
            return x
    
    if nums[-1]< target:
        return len(nums)
    
    if nums[0] >target:
        return 0
    
    for x in range(len(nums)):
        if(nums[x]<target and nums[x+1]>target):
            return x+1