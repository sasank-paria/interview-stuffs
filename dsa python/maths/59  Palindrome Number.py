'''9

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

'''
x = 234
print(x%10) -> 4
print(x//10) -> 23
'''


def isPalindrome():
    x = 121
    ori_num = x
    reversed = 0
    if x<0:
        return False
    else:
        while ori_num!=0:
            reversed = reversed*10 + ori_num%10
            ori_num = ori_num//10
    
        if reversed == x :
            return True
        else:
            return False


isPalindrome()
 
