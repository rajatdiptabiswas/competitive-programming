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
    
    private int rangeSumUtil(TreeNode node, int L, int R, int sum) {
        
        if ( node == null ) {
            return 0;
        }

        int returnSum = rangeSumUtil(node.left, L, R, sum);

        if ( node.val >= L && node.val <= R )
            returnSum += node.val;

        returnSum += rangeSumUtil(node.right, L, R, returnSum);

        return returnSum;
        
    }
    
    public int rangeSumBST(TreeNode root, int L, int R) {
        
        int sum = 0;
        
        return rangeSumUtil(root, L, R, sum);
        
        // if ( root == null )
        //     return 0;
        
        // if ( root.val >= L && root.val <= R )
        //     return root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R);
        
        // return rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R);
        
    }
    
}