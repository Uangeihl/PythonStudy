# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def help_101(left, right):
            if left and right:
                return left.val == right.val and help_101(left.left, right.right) and help_101(left.right, right.left)
            elif not left and not right:
                return True
            else:
                return False

        return help_101(root.left, root.right)
