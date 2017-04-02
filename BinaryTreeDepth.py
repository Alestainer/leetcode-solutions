__author__ = 'alestainer'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
        elif (root.left != None and root.right != None):
            return min(Solution().minDepth(root = root.left), Solution().minDepth(root = root.right)) + 1
        elif (root.left != None):
            return Solution().minDepth(root = root.left) + 1
        else:
            return Solution().minDepth(root= root.right) + 1