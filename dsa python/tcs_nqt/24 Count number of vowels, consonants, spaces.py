# Example 1:
# Input: string str=”Take u forward is Awesome”
# Output: 
# Vowels: 10
# Consonants: 11
# White spaces: 4


str = 'Take u forward is Awesome'
res = 0
for x in str:
    if x == 'a' or 'e' or 'i' or 'o' or 'u' :
        res+=1
        print(res)