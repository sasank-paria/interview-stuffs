# Example 1:
# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 
# Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.


def func(arr):
    arr.sort()
    map = {}

    for x in arr:
        map[x] = map.get(x,0) + 1
    print(map)

arr = [1,2,3,2,4,3,1,2]
func(arr)