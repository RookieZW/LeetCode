# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        nodes_val = []
        while len(nodes) > 0 or root:
            if root:
                nodes.append(root)
                root = root.left
                
            else:
                root = nodes.pop()
                nodes_val.append(root.val)
                root = root.right
        return nodes_val
'''
    双栈法
'''