class Solution:
    def isValid(self, s: str) -> bool:
        # dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        # stack = ['?']
        # for c in s:
        #     if c in dic:
        #         stack.append(c)
        #     elif dic[stack.pop()] != c:
        #         return False
        # return len(stack) == 1
        while True:
            l = len(s)
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
            if len(s) == l:
                break
        return len(s) == 0


solution = Solution()
print(solution.isValid("[{()}]"))
