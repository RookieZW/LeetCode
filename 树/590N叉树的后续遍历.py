"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        nodes_val = []
        if not root:
            return nodes_val
        res = [root,]
        while len(res) > 0:
            root  = res.pop()
            nodes_val.append(root.val)
            child = root.children
            nums = len(child)
            for i in range(nums):
                res.append(child[i])
        nodes_val.reverse()
        return nodes_val

'''
按照前序遍历的方式搞：
    需要改的孩子从左到右一个个加进去  最后反转
'''