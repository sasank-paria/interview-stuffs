# Example 1:
# Input: string = “google”
# Output: l,e

str = 'google'
map = {}
for x in str:
    map[x] = map.get(x,0) + 1

for x in map.keys():
    if map[x] ==1 :
        print(x,end='')