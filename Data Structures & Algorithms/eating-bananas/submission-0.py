import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        problem: given a list of piles, where the ith pile has 
        piles[i] amount of bananas, and a time limit in hours,
        given koko can eat k (int) bananas each hour, and 
        cannot eat from different piles in an hour, find
        the min value k

        h <= piles.length, the upper bound on k is the max number
        of bananas in a single pile, m

        binary search through 1 to m values through the list to see
        if its the min

        how do we verify min? 
        if koko cant complete --> shift upper bound
        if koko can complete --> check min, and shift lower bound
        """
        m = max(piles)

        min_k = float('inf')
        left, right = 1, m

        while left <= right:
            rate = (left + right) // 2 
            
            time = 0
            for bananas in piles:
                time += math.ceil(bananas/rate)

            if time <= h: # valid rate
                min_k = min(min_k, rate)
                right = rate - 1
            else:
                left = rate + 1
            # print(f"{min_k}, {rate}")

        return min_k

