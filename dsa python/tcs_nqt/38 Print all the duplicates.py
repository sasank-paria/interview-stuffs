# Example 1:
# Input:
#  str= "sinstriiintng"
# Output:
# i - 4
# n - 3
# s - 2
# t - 2
# Explanation:
# In the above example, 's' occurs twice, 'i' occurs four times, 't' occurs twice and 'n' occurs thrice. 'r' and 'g' occur only one time and hence are not considered.


str = 'sinstriiintng'
map = {}

for x in str:
    map[x] = map.get(x,0) + 1
print(map)

for x in map.keys():
    if map[x] > 1 :
        print(x,'-',map[x])

sort = sorted(map)
print(sort)