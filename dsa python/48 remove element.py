''' leetcode 27
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 The order of the elements may be changed. 
 Then return the number of elements in nums which are not equal to val.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

nums = [0,1,2,2,3,0,4,2]
val = 2

index = 0

for x in range(len(nums)):
    if nums[x]!=val:
        nums[index] = nums[x]
        index += 1

print(nums)
print(index)