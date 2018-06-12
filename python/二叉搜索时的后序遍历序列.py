# -*- coding:utf-8 -*-

'''
date:2018.3.27 21:50
author:song
'''

'''
题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        index = 0
        root = sequence[-1]
        length = len(sequence)
        '''  for循环求出i为什么不对？？  我知道了，，好好想想吧
        如果sequence中没有比root大的值，则i会一直
        for i in range(length - 1):
            if sequence[i] > root:
                break
        index = i
        '''
        while sequence[index] < root:
            index += 1

        for j in range(index, length - 1):
            if sequence[j] < root:
                return False

        left = right = True
        if index > 1:
            left = self.VerifySquenceOfBST(sequence[:index])
        if index < length - 2 and left:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return right