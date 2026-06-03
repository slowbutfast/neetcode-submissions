from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        given a list of temperatures, return a list where list[i] is the
        number of days where a warmer temperature is reached after n days

        use a stack. for each day, the temp to the temp at the top of the
        stack. if the temp is lower, add to the stack. if its greater, keep
        popping elements until its not
        """
        l = len(temperatures)
        res = [0] * l
        stack = deque()

        for i, temp in enumerate(temperatures):
            while stack:
                last_i, last_temp = stack[-1]
                if temp > last_temp:
                    stack.pop()
                    res[last_i] = i - last_i
                else:
                    break
            stack.append((i, temp))

        return res