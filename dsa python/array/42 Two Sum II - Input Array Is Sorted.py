''' leetcode 167
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

#two pointers  left at start and right at the end 

numbers = [2,7,11,15]
target = 9
#Output: [1,2]

left =0
right = len(numbers)-1

while left<right:
    current_sum=numbers[left]+numbers[right]

    if current_sum<target:
        left+=1
    elif current_sum>target:
        right-=1
    else:
        break

print([left+1,right+1])
    
    