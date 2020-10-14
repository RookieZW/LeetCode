# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        nodes_val = []
        while len(nodes) > 0 or root:
            if root:
                nodes.append(root)
                nodes_val.append(root.val)
                root = root.right
            else:
                root = nodes.pop()
                root = root.left
        nodes_val.reverse()
        return nodes_val