from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        maintain a frequency counter of letters in current window,
        but that are only found in t
        """
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""

        t_counts = Counter(t)
        ss_counts = {}
        valid_chars = set()

        min_str = ""
        min_len = float("inf")

        left = 0
        for right, char in enumerate(s):
            char_counts = ss_counts.get(char,0)
            ss_counts[char] = char_counts + 1

            if char in t_counts and char_counts+1 >= t_counts[char]:
                valid_chars.add(char)

            

            while len(valid_chars) == len(t_counts):
                ss_len = right - left + 2 # ss is s[left, right]
                if len(valid_chars) == len(t_counts) and ss_len < min_len:
                    min_str = s[left:right+1]
                    min_len = ss_len
                    
                l_char = s[left]
                ss_counts[l_char] -= 1
                if l_char in t_counts and ss_counts[l_char] < t_counts[l_char]:
                    valid_chars.remove(l_char)
                left += 1

        return min_str
                
            