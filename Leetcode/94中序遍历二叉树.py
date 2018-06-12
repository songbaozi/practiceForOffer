# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#非递归方法
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ret.append(node.val)
            root = node.right
        return ret


#递归方法
class Solution(object):
    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            self.ret.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)

        return self.ret
