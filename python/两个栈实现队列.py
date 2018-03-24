# -*- coding:utf-8 -*-

"""
date:2018.3.24
author:song
"""
"""
题目描述：
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, node):
        # write code here
        self.stackIn.append(node)

    def pop(self):
        # return xx
        # 用stackOut来保存队列出栈顺序的元素
        # 当stackOut不为空时，出stackOut的栈顶元素
        # 否则将stackIn中的元素以此压入stackOut中
        if self.stackOut:
            return self.stackOut.pop()
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()


"""
python中的list数据类型可以直接当作队列使用
queue = []
queue.append(node)  #在队列末尾添加元素，队列的进队操作
queue.pop(0)   #返回队列的第一个元素，队列的出队操作
"""