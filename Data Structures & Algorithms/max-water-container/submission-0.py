class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        use a left and right pointer. calculate the current amt
        of water held by container which is difference * min(left, right)

        when shrinking the window, shrink the bar that's smaller
        to maximize current height
        """
        l = len(heights)

        left, right = 0, l-1

        most_water = 0

        while left < right:
            left_h = heights[left]
            right_h = heights[right]

            curr_water = (right - left) * min(left_h, right_h)
            most_water = max(most_water, curr_water)

            if left_h < right_h:
                left += 1
            else:
                right -= 1

        return most_water