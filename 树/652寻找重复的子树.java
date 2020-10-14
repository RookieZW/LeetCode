/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private HashMap<String, Integer> memo = new HashMap<>(); 
    private LinkedList<TreeNode> res = new LinkedList<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {

        traverse(root);
        return res;
    }

    public String traverse(TreeNode root){
        if (root == null){
            return "#";
        }

        String left = traverse(root.left);
        String right = traverse(root.right);

        String subTree = left + "," + right + "," + root.val;

        int freq = memo.getOrDefault(subTree, 0); 
        if (freq == 1){
            res.add(root);
        }
        memo.put(subTree, freq+1);
        
        return subTree;

    }
}
/*
记录每组重复的根节点
    对每个出现的情况计数  防止多次重复出现
*/