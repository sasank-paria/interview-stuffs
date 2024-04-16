# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.


# str = 'TAKE U FORWARD'
str = 'ABCDCBA'

left,right = 0 , len(str)-1
res = bool

while left<right:
    if str[left]==str[right]:
        left+=1
        right-=1
    else:
        res = False
        print('not a palindrome')
        break

if res!= False:
    print('Palindrome')