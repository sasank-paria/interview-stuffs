# Example 1:
# Input: string str = "take12% *&u ^$#forward"
# Output: takeuforward
# Explanation:
# Characters 1,2,%,*,&,^,$,# along with whitespaces are 
# removed but the order of remaining alphabets is preserved.

str = 'take12% *&u ^$#forward'
res = ''
for x in str:
    if (x>='a' and x <= 'z') or (x>='A' and x <= 'Z'):
        res = res + x

print(res)