from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        given a string s1 and s2, we return true if we can find a 
        substring of s2 that is a permutation of s1. this means that
        substring is the same length as s1.
        """
        l_s1 = len(s1)
        l_s2 = len(s2)
        s1_counts = Counter(s1)
        ss_counts = Counter(s2[:l_s1])
        left = 0

        if ss_counts == s1_counts:
                return True

        # print(s1_counts)
        for right in range(l_s1, l_s2):
            char_to_add = s2[right]
            char_to_remove = s2[left]

            c_to_add = ss_counts.get(char_to_add,0)
            ss_counts[char_to_add] = c_to_add + 1

            c_to_remove = ss_counts.get(char_to_remove, 0)
            ss_counts[char_to_remove] = c_to_remove - 1
            if c_to_remove - 1 <= 0:
                del ss_counts[char_to_remove]

            # print(ss_counts)
            if ss_counts == s1_counts:
                return True
            
            left += 1

        return False