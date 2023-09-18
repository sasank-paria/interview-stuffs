class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Using two pointers approach to swap characters from both ends of the string until they meet at center
        left = 0
        right=len(s)-1

        while left<right:
            # swap characters at the two ends of string until they meet each other
            s[left],s[right]=s[right],s[left]
            # move towards center to avoid swapping same character again and again
            left=left+1
            right=right-1