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
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length-1);
    }
    
    public TreeNode helper(int[] nums, int start, int end){
        if(start > end) return null;
        int mid;
        if( (start+end) % 2 == 0){
            mid = (start+end)/2;
        }else{
            mid = (start+end)/2 + 1;
        }
        TreeNode root = new TreeNode(nums[mid]);
        root.left = helper(nums, start, mid-1);
        root.right = helper(nums, mid+1, end);
        return root;
    }
   
}