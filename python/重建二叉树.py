# -*- coding:utf-8 -*-

"""
date:2018.3.24
author:song
"""

"""
题目描述：
输入某二叉树的前序遍历和中序遍历的结果，
请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not tin or not pre:
            return None
        retRoot = TreeNode(pre.pop(0))
        index = tin.index(retRoot.val)
        retRoot.left = self.reConstructBinaryTree(pre,tin[:index])
        retRoot.right = self.reConstructBinaryTree(pre,tin[index+1:])
        return retRoot



"""
扩展：根据中序和后序遍历重建二叉树
"""
class Solution2:
    def reConstructBinaryTree(self,tin,post):
        if not tin or not post:
            return None
        retRoot = TreeNode(post.pop())
        index = tin.index(retRoot.val)
        retRoot.right = self.reConstructBinaryTree(tin[index + 1:], post)
        retRoot.left = self.reConstructBinaryTree(tin[:index],post)
        return retRoot

