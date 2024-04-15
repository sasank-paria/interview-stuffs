# Example 1:
# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Example 2:
# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0


def func(arr):
    middle = 1
    temparr = [0] + arr + [0]          # [0,1,-1,4,0]
    
    while middle <= len(arr) :
        sumleft = sum(temparr[0:middle])
        sumright = sum(temparr[middle+1 : len(temparr)])
        if sumleft == sumright :
            print(middle-1)
            break
        sumleft = 0
        sumright = 0
        middle+=1

arr = [1,-1,4]
arr2 =  [2,3,-1,8,4]
func(arr2)