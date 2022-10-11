import re


class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        # str = s.split(' ')
        # for string in str[len(str):0:-1]:
        #     l = len(string)
        #     if l != 0:
        #         return l
        # return len(str[0])
        count = 0
        for ch in s[::-1]:
            if ch != ' ':
                count += 1
            if count != 0 and ch == ' ':
                break
        return count


print(Solution.lengthOfLastWord("   fly me   to   the moon  "))
