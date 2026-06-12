class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string s, and an integer k that represents how
        many characters we can replace. return the length
        of the longest substring that contains only one character,
        with k replacements

        the number of characters we can replace is the most frequent
        letter in the substring - k. use a sliding window with counter
        of elements in the window. shrink window while condition is
        invalid.

        maxf - length of longest string

        invalid condition:
        while ss_length - maxf > k:
        """
        counter = {}
        left = maxf = longest = 0

        for right, char in enumerate(s):
            counter[char] = counter.get(char, 0) + 1

            maxf = max(maxf, counter[char])

            while (right - left + 1) - maxf > k:
                counter[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest