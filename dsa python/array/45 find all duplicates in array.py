''' leetcode 442
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
'''

# nums = [4,3,2,7,8,2,3,1]

# duplicate = []

# for x in nums:
#     if nums.count(x)>1 and x not in duplicate:
#         duplicate.append(x)

# print(duplicate)  
# time limit exceeded




nums = [4,3,2,7,8,2,3,1]
nums.sort()
duplicate = []
x,y=0,1

while y<len(nums):
    if nums[x]==nums[y]:
        duplicate.append(nums[y])

    x+=1
    y+=1

print(duplicate)

