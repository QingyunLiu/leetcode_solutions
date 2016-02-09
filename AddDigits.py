#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

"""
11->2
121->4
也就是(11-2)能被9整除，(121-4)能被9整除
即(n-x)%9=0, 其中x为数根, n为原始数字

设(n-x)/9 = k
则x = n-9k
即x = n - 9*((n-1)/9)
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        return int(num - ((num-1)/9)*9)
