# -*- coding:utf-8 -*-

'''
date:2018.3.28 15:47
update:2018.3.30 21:30
author:song
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#采用中序遍历的非递归解法
class Solution:
    def Convert(self, pRootOfTree):
        # write code here 非递归版本
        if not pRootOfTree:
            return
        stack = []
        p = pRootOfTree
        isFirst = True
        root = p
        pre = p
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if isFirst:
                root = p
                pre = root
                isFirst = False
            else:
                pre.right = p
                p.left = pre
                pre = p
            p = p.right
        return root


#递归解法
class Solution2:
    def Convert(self, root):
        # write code here递归解法
        if not root:
            return
        if not root.left and not root.right:
            return root
        left = self.Convert(root.left)
        p = left
        while p and p.right:
            p = p.right
        if left:
            p.right = root
            root.left = p

        rightNode = self.Convert(root.right)
        if rightNode:
            root.right = rightNode
            rightNode.left = root

        if left:
            return left
        else:
            return root