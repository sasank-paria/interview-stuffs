# Example 1:
# Input: String str1 = “abcdef”
#        String str2 = “cefz”
# Output: abd
# Explanation: The common characters in both strings are c, e, f.
# So after removing these characters from string 1 we get string resulting string as abd.

str1 = 'abcdef'
str2 = 'cefz'
res = ''

# for x in str2:
#     while x in str1 :
#         str1 = str1.replace(x,'')   #it will replace it with empty string . also see the variable storing that is same it is.
# print(str1)

for x in str1:
    if x in str2 :
        res = res + ''
    else:
        res = res + x
print(res)