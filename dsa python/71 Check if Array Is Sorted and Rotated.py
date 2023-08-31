'''1752

Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). 
Otherwise, return false.

There may be duplicates in the original array.


Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
'''


#check if the previous value is smaller in array and also compare first and last value of the array. 


def check():
    nums = [3,4,5,1,2]
    count = 0
    for index in range(0,len(nums)):
        if (nums[index]<nums[index+1]):
            count = count+1
        
    if (nums[0]>nums[len(nums)-1]):
        count = count+1