# Example 1:
# Input: “a+((b-c)+d)”
# Output: “a+b-c+d”
# Explanation: Removed all the brackets in the algebric expression.

str = 'a+((b-c)+d)'
brackets = ['(',')']
res = ''

for x in str:
    if x in brackets:
        res = res
    else:
        res = res + x
print(res)