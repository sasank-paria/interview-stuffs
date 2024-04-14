# Example 1:
# Input: 
# Arr[] = [1,1,2,3,4,4,5,2]
# Output:
#  1,2,4
# Explanation:
#  1,2 and 4 are the elements which are occurring more than once.


def func(arr):
    map = {}
    res = []

    for x in arr:
        map[x] = map.get(x,0) + 1
    print(map)

    for y in map.keys():
        if map.get(y)>1 :
            res.append(y)
    print(res)


arr = [1,1,2,3,4,4,5,2]
func(arr)