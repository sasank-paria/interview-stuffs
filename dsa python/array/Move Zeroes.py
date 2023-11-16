'''283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

 def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        big O of n square soln :

        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]==0:
                    nums[x],nums[y]=nums[y],nums[x]

        return nums

        """

    # try to move non zero to the left instead of moving zeroes to the right !

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1