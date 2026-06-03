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
        left = 0

        # print(s1_counts)
        for right in range(l_s1, l_s2+1):
            substring = s2[left:right]
            ss_counts = Counter(substring)

            # print(ss_counts)
            if ss_counts == s1_counts:
                return True
            
            left += 1

        return False