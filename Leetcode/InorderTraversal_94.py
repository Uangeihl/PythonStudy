# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.help_94(root, res)
        return res

    def help_94(self, root, res):
        if not root: return
        self.help_94(root.left, res)
        res.append(root.val)
        self.help_94(root.right, res)
        return res
