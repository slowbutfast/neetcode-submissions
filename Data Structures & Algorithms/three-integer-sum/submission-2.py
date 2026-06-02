class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        two pointer, where we increment through the list
        '''

        l = len(nums)
        nums.sort()
        res = []

        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, l - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return res