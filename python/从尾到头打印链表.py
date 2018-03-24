# -*- coding:utf-8 -*-

'''
date:2018.3.23
author:song
'''

'''
题目描述：
输入一个链表，从尾到头打印链表每个节点的值。
'''



# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        #遍历链表将值以此存入栈，然后以此出栈打印
        ret = []
        while listNode:
            ret.insert(0,listNode.val)
            listNode = listNode.next
        return ret

        '''
        while listNode:
            ret.append(listNode.val)
            listNode = listNode.next
        return ret[::-1]
        '''