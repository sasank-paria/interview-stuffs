'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Input: nums = [3,0,1]
Output: 2
**Note: The array must be sorted for this to work. Use arr.sort() on an unsorted array before feeding it to the program.
'''

arr = [3,4,2,6]
arr.sort()
missing_elements = []

for x in range(arr[0],arr[-1]+1):
    if x not in arr:
        missing_elements.append(x)

print(missing_elements)

