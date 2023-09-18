''''383

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''


def ransomnote():
    ransomNote = "fihjjjjei"
    magazine = "hjibagacbhadfaefdjaeaebgi"

    map_magazine = {}
    map_ransom = {}

    for c2 in magazine:
        map_magazine[c2] = 1 + map_magazine.get(c2,0)
    print("magazine",map_magazine)
    
    for c1 in ransomNote:
        map_ransom[c1] = 1 + map_ransom.get(c1,0)
    print('ransom',map_ransom)

    for c1 in ransomNote:
        if map_ransom.get(c1,0) <= map_magazine.get(c1,0):
            return True
        else:
            return False

ransomnote()