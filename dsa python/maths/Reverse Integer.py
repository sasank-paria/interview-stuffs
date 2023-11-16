''' 7
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

def reverse(self, x: int) -> int:
        if x<0:
            x = x*-1
            number = str(x)
            reverse = number[::-1]
            res = int(reverse) * -1
        else:
            number = str(x)
            reverse = number[::-1]
            res = int(reverse)
        
        if res >2**31 -1 or res< -2**31:
            return 0

        return res