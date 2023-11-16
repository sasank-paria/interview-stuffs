'''485
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        r = 0
        count = 0
        max_count = 0

        if len(nums)==1 and nums[0]==1:
            return len(nums)
        if len(nums)==1 and nums[0]!=1:
            return 0

        while r<len(nums):
            if nums[r] == 1:
                count = count+ nums[r] 
                
            else :
                count = 0
                
            max_count = max(max_count , count)
            r+=1

        return max_count