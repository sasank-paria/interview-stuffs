# Problem: Given a string, calculate the sum of numbers in a string (multiple consecutive digits are considered one number)

# Examples:

# Example 1:
# Input: string = “123xyz”
# Output: 123

# Example 2:
# Input: string = “1xyz23”
# Output: 24


str = '1xyz23'
res = 0
temp = '0'
for x in str:
    if x.isdigit():
        temp = temp + x  #it is because still nos are in string form
        print(temp)
    else:
        res = res + int(temp)
        temp= '0'
    
print(res)

