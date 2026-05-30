from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack of previously seen elements, (val, index)

        pop all vals smaller than value at current index. append 
        to res array with the difference between curr index and smaller index
        """

        stack = deque()
        res = [0] * len(temperatures)

        for curr_index, curr_val in enumerate(temperatures):
            while stack:
                peek_val, _ = stack[-1]

                if peek_val < curr_val:
                    _, peek_index = stack.pop()
                    res[peek_index] = (curr_index - peek_index)
                else:
                    break
            stack.append((curr_val, curr_index))

        return res