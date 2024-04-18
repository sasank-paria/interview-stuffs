# Example 1:
# Input: string str=”Take u forward is Awesome”
# Output: 
# Vowels: 10
# Consonants: 11
# White spaces: 4


str = 'Take u forward is Awesome'
vowels = 0
consonants = 0
whitespace = 0

for x in str:
    char = x.lower()
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' :
        vowels+=1
    elif char == " " :
        whitespace+=1
    else:
        consonants+=1

print(vowels,consonants,whitespace)