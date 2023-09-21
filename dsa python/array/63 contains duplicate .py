'''217

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
#two pointers method 

def containsDuplicate() :
    #nums = [1,2,3,4,1]
    nums = [3,3]

    if len(nums)==1:
        return False
    else:
        nums.sort()
        l,r=0,1
        while r<=len(nums)-1:
            if nums[l]==nums[r]:
                return True
            l+=1
            r+=1
    return False

containsDuplicate()