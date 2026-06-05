class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        binary search
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + ((right-left)//2)
            m_num = nums[middle]

            if m_num == target:
                return middle
            elif m_num < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1