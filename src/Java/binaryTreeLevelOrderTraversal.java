/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> order = new ArrayList<List<Integer>>();
        int maxHeight = maxDepth(root);
        for(int level=1;level<=maxHeight;level++){
            List<Integer> singleLevel = new ArrayList<>();
            levelOrder(root, singleLevel, level);
            order.add(singleLevel);
        }
        
        return order;
        
    }
    
    public void levelOrder(TreeNode root, List<Integer> levelList, int level) {
        if(root == null) return;
        
        if(level == 1){
            levelList.add(root.val);
        }else{
            levelOrder(root.left, levelList, level-1);
            levelOrder(root.right, levelList, level-1);
        }
    }
    
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        int max = left > right ? left : right;
        return max+1;
    }
}