class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string and an integer k, return the length
        of the longest substring of only one character, given we
        can replace k characters

        maintain a hashmap of frequency of the current window.

        length of window - most frequent character = # of replacements

        how do we know most frequent chars? — doesn't matter. we 
        only care if we find a greater maxf than the previous maxf

        shrink window till valid
        """

        l = len(s)
        counts = {}
        maxf = 0 # current character count for the largest window so far
        longest = 0

        left = 0
        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            maxf = max(maxf, counts[char])

            while (right - left + 1) - maxf > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
            