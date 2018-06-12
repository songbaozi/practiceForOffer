# -*- coding:utf-8 -*-

'''
date:2018.3.27 19:48
author:song
'''

'''
题目描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''



# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        queue = []
        retList = []
        if not root:
            return []
        queue.append(root)
        retList.append(root.val)
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                retList.append(cur.left.val)
            if cur.right:
                queue.append(cur.right)
                retList.append(cur.right.val)
        return retList