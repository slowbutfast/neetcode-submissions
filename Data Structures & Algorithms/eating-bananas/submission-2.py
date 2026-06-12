import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        given an array of piles, where piles[i] represents the number
        of bananas in that pile, and an int h, that represents
        the number of hours we have to eat all the bananas, return
        the minimum banana eating rate (as an integer)

        upper bound is the max amount of bananas in one pile
        lower bound is 1

        iterate through all eating speeds, looping through the 
        array, calculating the minimum valid eating speed

        normal loop is O(n^2) time, but we can use binary
        search through valid rates for O(nlogm time)
        """
        maxb = max(piles) # max number of bananas in one pile
        min_speed = maxb

        left, right = 1, maxb
        while left <= right:
            rate = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            # print(rate)
            if time <= h:
                min_speed = min(min_speed, rate)
                # valid rate, so we move the right bound 
                # to try to get faster
                right = rate - 1
            else:
                left = rate + 1

        return min_speed