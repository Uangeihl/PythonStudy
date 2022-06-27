class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        while len(n) > 1:
            n_sum = 0
            for e in n:
                n_sum += int(e)
            n = str(n_sum)
        return int(n)


print(Solution().addDigits(38))
