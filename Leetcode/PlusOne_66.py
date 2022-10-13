class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            if flag == 0:
                break
            digits[i] += flag
            if digits[i] == 10:
                flag = 1
                digits[i] = 0
            else:
                flag = 0
        if flag == 1:
            return [1] + digits
        else:
            return digits


s = Solution()
print(s.plusOne([9]))
