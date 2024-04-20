# Example 1:
# Input: s = "bcabc"
# Output: “bca"

# Explanation: Duplicate Characters are removed
# Example 2:
# Input: s = "cbacdcbc"
# Output: "cbad" 
# Explanation: Duplicate Characters are removed


str = 'cbacdcbc'
map = {}
res = ''

for x in str:
    map[x] = map.get(x,0) + 1

for x in map.keys():
    res = res + x
print(res)