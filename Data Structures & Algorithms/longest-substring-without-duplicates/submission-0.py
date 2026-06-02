class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window:
            increase window size as much as possible until we reach
            a duplicate letter

            when we reach a duplicate, shrink window until we 
            reach the duplicate
        """
        window = set()
        l = len(s)
        left = 0
        maxx = 0

        for right, char in enumerate(s):
            if char in window:
                # shrink window until duplicate
                while char in window:
                    window.remove(s[left])
                    left += 1

            window.add(char)

            # length of string is [left, right)
            maxx = max(maxx, right - left + 1)

        return maxx