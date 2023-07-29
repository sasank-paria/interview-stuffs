'''238

Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# def productExceptSelf():
#     nums = [1,2,3,4]
#     res = []
#     print(nums)
#     if len(nums)==1 :
#         print(nums)
#         return nums
#     else:
#         x=0
#         while x<len(nums):
#             multiplier = 1
#             print(multiplier)
#             for y in range(0,len(nums)):
#                 if y == x :
#                     pass
#                 else:
#                     multiplier = multiplier * nums[y]
#             print(multiplier)
#             res.append(multiplier)
#             x+=1
#     print(res)
#     return res

# productExceptSelf()





