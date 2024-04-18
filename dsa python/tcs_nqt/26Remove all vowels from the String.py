# Example 1:
# Input: Str = “take u forward”
# Output: tk  frwrd
# Explanation: All vowels are removed from the given String.

# Example 2:
# Input: Str = “I am very happy today”
# Output:  m vry happy tdy
# Explanation: All vowels are removed from the given String.

'''  
# Initializing String
test_str = "GeeksForGeeks"
 
# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')
 
# Printing string after removal
# removes all occurrences of 'e'
print("The string after removal of i'th character( doesn't work) : " + new_str)
 
# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)
'''


str = 'take u forward'
newstr = ''

for x in str:
    char = x.lower()
    if char!='a' or char!='e' or char!='i' or char!='o' or char!='u' :
        newstr = newstr + x
        print(newstr)