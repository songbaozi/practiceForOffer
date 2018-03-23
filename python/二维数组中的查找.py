# -*- coding:utf-8 -*-

'''
date:2018.3.23
author:song
'''

'''
题目描述：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows=len(array)
        columns=len(array[0])
        r=0
        c=columns-1
        while(r<rows and c>-1):
                if array[r][c]==target:
                    return True
                elif array[r][c]>target:
                    c=c-1
                else:
                    r=r+1
        return False