# _*_ coding:utf-8 _*_

'''
date:2018.3.24
update:2018.3.27 19.40
author：song
'''

'''
题目描述：操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''

'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
'''

class Solution:
    def Mirror(self,root):
        #利用递归解决
        if root:
            tempNode = root.left
            root.left = root.right
            root.right = tempNode
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root