# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false 
 '''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapping = {']':'[',')':'(','}':'{'}
        for char in s :
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
         
         # If the string is valid then at end of loop we should have an empty list as remaining
        return True if not stack else False