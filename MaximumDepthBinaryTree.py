#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Question:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            dep_left = self.maxDepth(root.left)
            dep_right = self.maxDepth(root.right)
            return max(dep_left, dep_right)+1
        """
        if root.left is None and root.right is None:
            return 1
        elif root.left is None and root.right is not None:
            return self.maxDepth(root.right)+1
        elif root.left is not None and root.right is None:
            return self.maxDepth(root.left)+1
        elif root.left is not None and root.right is not None:
            dep_left = self.maxDepth(root.left)
            dep_right = self.maxDepth(root.right)
            return max(dep_left, dep_right)+1
        """

"""
递归求深度
注意:
1. root为None的情况
2. 子节点为None时，无left、right节点
3. 在类函数中递归调用自身须使用self：self.maxDepth，否则会被当做调用全局函数maxDepth
"""
