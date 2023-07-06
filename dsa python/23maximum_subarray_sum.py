'''
Given an integer array nums, find the subarray with the largest sum, and return its sum
A subarray is a A subarray is a contiguous non-empty sequence of elements within an array. of elements within an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
'''
###kadane's algorithm

nums = [-2,1,-3,4,-1,2,1,-5,4]
cur_sum = 0
max_sum = 0

for x in range(0,len(nums)):
    cur_sum += nums[x]
    if (cur_sum > max_sum):
        max_sum = cur_sum
    if (cur_sum<0):
        #reset current sum to zero as we are moving towards negative values
        cur_sum = 0

print(max_sum)