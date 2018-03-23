# -*- coding:utf-8 -*-

'''
date:2018.3.23
author:song
'''

'''
题目描述：
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution1:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #遍历原字符串，，，找出有几个空格，则可确定替换后字符串的长度
        listS = list(s)
        count = 0
        for i in range(len(listS)):
            if listS[i] == ' ':
                count += 1
        newList = [0]*(len(listS) + count*2)
        index = len(listS) - 1
        indexNew = len(newList) - 1
        while index > -1 and indexNew > -1:
            if listS[index] == ' ':
                newList[indexNew] = '0'
                newList[indexNew-1] = '2'
                newList[indexNew-2] = '%'
                indexNew -= 3
                index -= 1
            else:
                newList[indexNew] = listS[index]
                indexNew -= 1
                index -= 1
        return ''.join(newList)



# -*- coding:utf-8 -*-
class Solution2:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #将字符串转为数组，遍历数组发现空格，则直接替换为%20
        #最后再将数组转为字符串返回
        listS = list(s)
        length = len(listS)
        for i in range(length):
            if listS[i] == ' ':
                listS[i] = '%20'
        return ''.join(listS)