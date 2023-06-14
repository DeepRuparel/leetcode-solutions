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
    List<Integer> nodeValues = new ArrayList<>();
    void dfs(TreeNode root){
        if(root == null){
            return;
        }
        
        dfs(root.left);
        nodeValues.add(root.val);
        dfs(root.right);
        
    }
    public int getMinimumDifference(TreeNode root) {
        dfs(root);
        int ans = Integer.MAX_VALUE;
        for(int i = 1; i < nodeValues.size(); i++){
            if (Math.abs(nodeValues.get(i) - nodeValues.get(i-1)) < ans){
                ans = Math.abs(nodeValues.get(i) - nodeValues.get(i-1));
            }
        }
        return ans;
            
        
    }
}