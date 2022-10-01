class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # sum = 0
        # temp = x
        # while temp > 0:
        #     sum = sum * 10 + temp % 10
        #     temp /= 10
        # return sum == x
        return str(x) == str(x)[::-1]


solution = Solution()
print(solution.isPalindrome(121))
