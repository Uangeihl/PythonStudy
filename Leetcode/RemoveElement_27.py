import math


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left] = nums[right]
                right -= 1
        return left


s = Solution()
print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
