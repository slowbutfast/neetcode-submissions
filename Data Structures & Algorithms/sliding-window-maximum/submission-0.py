from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        we maintain a max heap that contains all the elements in the current
        window. we then append the current heap max to the res list.

        nevermind. we just sort the window at every step, appending
        the largest value. use a queue to handle 
        """
        window = deque()
        res = []

        for i in range(k):
            window.append(nums[i])

        sorted_window = sorted(window)
        res.append(sorted_window[-1])

        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])

            sorted_window = sorted(window)
            res.append(sorted_window[-1])

        return res