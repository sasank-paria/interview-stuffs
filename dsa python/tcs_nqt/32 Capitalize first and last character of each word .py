# Example 1:
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string



str = "take u forward is awesome"
words = str.split()  #extracting words from a string
res = ''
finalres = ''

for x in words:
    if len(x)==1:
        res= x.capitalize()
        finalres = finalres + ' ' + res
    else:
        res = x[0].capitalize() + x[1:-1] + x[-1].capitalize()
        finalres = finalres + ' ' + res
        
print(finalres)

