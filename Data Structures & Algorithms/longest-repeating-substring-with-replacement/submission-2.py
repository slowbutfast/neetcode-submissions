class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string s and an int k, we can replace up to k
        letters and replace them with any letter. we have to return
        the length of the longest substring that contains
        only one distinct characters

        we can use a sliding window to track frequency of window.
        then calculate available replacements by subtracting
        length of window by most frequent char in window

        # of replacements = most freq - len

        1. initialize left pointer
        2. for loop through list with right pointer
        3. each iteration, calculate longest string with
            maxf + k where maxf is longest character frequency
        4. shrink window till vaild 
        """
        left = 0
        maxf = 0
        longest = 0
        window_count = {}

        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1

            maxf = max(maxf, window_count[char])

            while (right - left + 1) - maxf>  k:
                window_count[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)

        return longest
