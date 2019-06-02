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
    
    public void printReverseInorder(TreeNode root) {
        
        if (root == null) return;
        
        printReverseInorder(root.right);
        System.out.println(root.val);
        printReverseInorder(root.left);
        
    }
    
    public int bstToGstUtil(TreeNode node, int sum) {
        
        if (node == null)
            return sum;
        
        int returnSum = bstToGstUtil(node.right, sum);
        
        returnSum += node.val;
        // System.out.print(returnSum + " ");
        node.val = returnSum;
        
        returnSum = bstToGstUtil(node.left, returnSum);
        
        return returnSum;
        
    } 
    
    public TreeNode bstToGst(TreeNode root) {
        
        // printReverseInorder(root);
        
        int sum = 0;
        bstToGstUtil(root, sum);
        
        return root;
        
    }
    
}