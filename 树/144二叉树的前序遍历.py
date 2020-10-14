# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        nodes_val = []
        while len(nodes) > 0 or root:
            if root:
                nodes.append(root)
                nodes_val.append(root.val)
                root = root.left
            else:
                root = nodes.pop()
                root = root.right
        return nodes_val