'''169

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
nums = [2,2,1,1,1,2,2]
counter = {}   #using hash map
maxcount=0

for x in nums :
    counter[x] = 1 + counter.get(x,0)
    res = x if counter[x] > maxcount else res 

    maxcount = max(counter[x],maxcount)

print(res)






