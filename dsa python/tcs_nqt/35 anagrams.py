# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.

str1 = 'RULES'
str2 = 'LESRT'

map1 = {}
map2 = {}

if len(str1)!=len(str2):
    print('false')
else:

    for x,y in zip(str1,str2):
        map1[x] = map1.get(x,0) + 1
        map2[y] = map2.get(y,0) + 1
    
    for x in str1:
        if map1[x] != map2.get(x,0):
            print('false')

    print('true')
