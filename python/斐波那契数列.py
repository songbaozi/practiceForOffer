# -*- coding:utf-8 -*-

'''
date:2018.3.25
author:song
'''

'''
题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        # write code here 0 1 1 2
        F = [0,1,1,2]
        if n <= 3:
            return F[n]
        for i in range(4,n+1):
            F.append(F[i-1] + F[i-2])
        return F[n]