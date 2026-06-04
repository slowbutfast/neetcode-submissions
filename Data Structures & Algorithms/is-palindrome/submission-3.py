class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        left, right pointer

        just compare if s[left] == s[right]

        we need to lowercase the string 
        """
        l = len(s)
        left, right = 0, l-1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
        
        return True