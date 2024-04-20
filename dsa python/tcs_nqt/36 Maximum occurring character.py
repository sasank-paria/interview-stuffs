# Example 1:
# Input: str = “takeuforward”
# Output: a
# Explanation: The character 'a' and 'r’ have the same  maximum occurrence i.e 2. Hence we can print any one of them

# Example 2:
# Input: str = “apple”
# Output: p
# Explanation: The character 'p' have the maximum occurrence i.e 2.


str = 'takeuforward'
map = {}
value = 0
res = 0

for x in str:
    map[x] = map.get(x,0) + 1

for x in str:
    value = map.get(x,0)
    res = max(res,value)

for i in map.keys():
    if map[i] == res :
        print(i)