# Example 1:
# Input: takeuforward
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
# Explanation: Count of every character of string is printed.


str = 'takeuforward'
map = {}

for x in str:
    map[x] = map.get(x,0) + 1

for x in map.keys():
    print(x,map[x],' ',sep='',end='')  # sep='' is used to avoid the space between variablew sep means separator