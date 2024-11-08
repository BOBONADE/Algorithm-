#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm- 
@File    ：3110. Score of a String.py
@Author  ：Bobby
@Date    ：08/11/2024 18:53 
'''



'''
how to change char to ascII int: chr('a') -> 97
the python abs() function: abs(-2) -> 2

'''
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            ans += abs(ord(s[i]) - ord(s[i + 1]))

        return ans


obj = Solution()
print(obj.scoreOfString(s="hello"))
print(obj.scoreOfString(s="zaz"))
