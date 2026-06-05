"""
we need to design a stack with push, pop, top (peek), and getMin which
tells us the minimum element currently in the stack.

key: keep track of the min element in the stack. we can track the min
at every point using a second stack

similar to the # days till new max temp. we need a monotonically 
decreasing stack

- init will init two empty stacks
- every time we push, we check if the new element is smaller than the 
previous max. if so, we push that element into the stack.
- when we pop, we just pop from both lists. the second stack tracks
the greatest element at the current moment
- getMin returns the top of the second stack
"""
from collections import deque
class MinStack:

    def __init__(self):
        self.user_stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if self.min_stack:
            curr_top = self.min_stack[-1]
            curr_min = val if val < curr_top else curr_top
            self.min_stack.append(curr_min)
            self.user_stack.append(val)
        else:
            self.min_stack.append(val)
            self.user_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.user_stack.pop()

    def top(self) -> int:
        return self.user_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
