class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        binary search
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            middle_num = nums[middle]

            if middle_num == target:
                return middle
            elif middle_num > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1