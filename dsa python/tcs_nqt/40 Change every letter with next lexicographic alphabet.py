# Problem Statement: Given a string, write a program to change every letter in the given string with the letter following it in the alphabet (ie. a becomes b, p becomes q, z becomes a)

# Examples:

# Example 1:
# Input: string str = “abcdxyz”
# Output: bcdeyza


str = 'abcdxyz'
res = ''
for x in str:
    if x == 'z' :
        res = res + 'a'
    else:
        res = res + chr(ord(x)+1)    #used chr() and ord() function ord function gives asci value

print(res)