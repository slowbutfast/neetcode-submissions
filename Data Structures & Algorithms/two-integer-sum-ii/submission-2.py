class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        use left and right pointer. calculate sum at every step.
        if sum is correct, return it; if sum is less than target,
        increment left, and if sum is greater than target, inc right

        and we return the 1-indexed index
        """
        l = len(numbers)
        left, right = 0, l-1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1