"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        s = []
        if not root:
            return s
        s.append(root)
        res_val = []
        while len(s) > 0:
            root = s.pop()
            res_val.append(root.val)
            child = root.children
            nums = len(child)
            for i in range(nums - 1, -1, -1):
                s.append(child[i])
        return res_val
'''
单栈：
    孩子需要全部加入到后面  然后再pop
'''