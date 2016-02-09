#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
"""


"""
当1<=n<=3时，先手必胜
当n=4时，先手比输
当n=5时，先取1个，让对方处于先手4个情况。先手必胜
当n=6时，先取2个，让对方处于先手4个情况。先手必胜
当n=7时，先取3个，让对方处于先手4个情况。先手必胜
当n=8时，无论先取几个，问题都将简化为5<=n<=7时，对手先手的情况。先手必输
当n=9时，先取1个，让对方处于先手8个情况。先手必胜
......
可知，n能被4整除时，先手必输；否则必胜
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4>0        
