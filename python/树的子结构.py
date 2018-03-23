# -*- coding:utf-8 -*-

"""
date:2018.3.23
author:song
"""

'''
题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        # 先找到A中与B的根节点相同的节点
        result = False
        if pRoot1.val == pRoot2.val:
            #如果节点相同，以此判断其下方的子树是否相等
            result = self.doesTree1IsTree2(pRoot1, pRoot2)
        if not result:
            #如果没有找到相等的跟节点，递归左子树
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            #如果左子树也不相等，递归调用右子树
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def doesTree1IsTree2(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.doesTree1IsTree2(root1.left, root2.left) \
               and self.doesTree1IsTree2(root1.right, root2.right)