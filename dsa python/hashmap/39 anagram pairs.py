'''242
xample 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

# using hash map #


def isAnagram(s: str, t: str) -> bool:
    maps = {}
    mapt = {}
    if len(s)!=len(t):
        return False
    else:
        for c1 , c2 in zip(s,t):
            maps[c1] = maps.get(c1,0)+1
            mapt[c2] = mapt.get(c2,0)+1
        
        for c1 in s :
            if maps[c1]!=mapt.get(c1,0) :
                return False
    return True
            
        

s = "anagram"
t = "nagaram"
isAnagram(s,t)