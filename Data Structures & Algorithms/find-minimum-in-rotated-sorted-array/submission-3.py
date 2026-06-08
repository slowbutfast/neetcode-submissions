class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right:
            middle = (left + right )//2 
            left_num = nums[left]
            right_num = nums[right]
            middle_num = nums[middle]

            if middle_num < right_num:
                right = middle
            else:
                left = middle + 1

            # print(f"{left} {right}")

        return nums[left]
        