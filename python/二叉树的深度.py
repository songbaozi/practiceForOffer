'''
date:2018.3.28 17:18
author:song
'''

'''
题目描述：
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #递归解法
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if left > right:
            return left+1
        else:
            return right+1

    #非递归解法
    def TreeDepth2(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        depth = count = 0
        curCount = 1
        queue = []
        queue.append(pRoot)
        while queue:
            node = queue.pop(0)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if count == curCount:
                depth += 1
                curCount = len(queue)
                count = 0
        return depth