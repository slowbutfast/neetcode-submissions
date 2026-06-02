class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointer. increment left when sum less than target, decrement
        right when sum greater than target
        """

        l = len(numbers)
        left, right = 0, l - 1

        total = numbers[left] + numbers[right]

        while total != target:
            if total < target:
                left += 1
            elif total > target:
                right -= 1

            total = numbers[left] + numbers[right]

        return [left + 1, right + 1]