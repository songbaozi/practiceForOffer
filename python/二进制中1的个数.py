# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        return bin(n).count('1')


'''
C++/java中的解法

class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         while(n){
             ++count;
             n = (n - 1) & n;
         }
         return count;
     }
};


'''