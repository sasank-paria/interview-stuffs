'''290

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

'''

def wordPattern(pattern: str, s: str) -> bool:
    words=s.split()

    map_pattern_to_s = {}
    map_s_to_pattern = {}

    if len(words)!=len(pattern):
        return False
    else:
        for c1 , c2 in zip(pattern,words):
            if (c1 in map_pattern_to_s and map_pattern_to_s[c1]!=c2)or(c2 in map_s_to_pattern and map_s_to_pattern[c2]!=c1) :
                return False
            map_pattern_to_s[c1] = c2
            map_s_to_pattern[c2] = c1
        return True