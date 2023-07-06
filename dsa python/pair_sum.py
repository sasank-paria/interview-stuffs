'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,3], target = 6
Output: [0,2]

Input: nums = [3,3], target = 6
Output: [0,1]
'''

nums = [3,2,3]
target = 6

for x in range(0,len(nums)-1):
    for y in range(x+1, len(nums)):
        addition=nums[x]+nums[y]
        if  addition==target:
            print(x,y)
            


