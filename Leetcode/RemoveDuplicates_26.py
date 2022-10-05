from ast import List


# class Solution:
#     def removeDuplicates(self, nums):
#         count = 0
#         for i in range(len(nums)-1):
#             if nums[i+1] != nums[count]:
#                 count += 1
#                 nums[count] = nums[i+1]
#         return count+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        for _ in nums:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))
