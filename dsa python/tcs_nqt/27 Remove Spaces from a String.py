# Example 1:
# Input: str = “Take you forward” 
# Output: Takeyouforward

str = 'Take you forward'
res = ''

for x in str:
    if x == ' ' :
        res = res
    else:
        res = res +  x

print(res)