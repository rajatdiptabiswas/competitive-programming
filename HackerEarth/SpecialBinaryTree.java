// https://leetcode.com/discuss/interview-question/363945/google-special-binary-tree

import java.util.*;
import java.lang.*;
import java.io.*;

class TreeNode
{
    private int A, B;
    public TreeNode left = null, right = null;

    public TreeNode(int A, int B) {
        this.A = A;
        this.B = B;
    }

    public int getA() { return A; }
    public int getB() { return B; }
}
class Pair
{
    private int A, B;
    public Pair(int A, int B) {
        this.A = A;
        this.B = B;
    }

    public int getA() { return A; }
    public int getB() { return B; }
}

class Compare implements Comparator<Pair>
{
    public int compare(Pair a, Pair b) {
        return (a.getA() - b.getA());
    }
}

public class SpecialBinaryTree
{
    public static TreeNode algorithm(ArrayList<Pair> nodes, int start, int end)
    {
        if(start > end) return null;

        Pair maxPair = nodes.get(start);
        int mid = start;
        for(int i = start + 1; i <= end; i++) {
            if(maxPair.getB() < nodes.get(i).getB()) {
                maxPair = nodes.get(i);
                mid = i;
            }
        }

        TreeNode head = new TreeNode(maxPair.getA(), maxPair.getB());

        head.left = algorithm(nodes, start, mid-1);
        head.right = algorithm(nodes, mid+1, end);

        return head;
    }

    public static void prettyPrintTree(TreeNode node, String prefix, boolean isLeft) {
        if (node == null) {
            System.out.println("Empty tree");
            return;
        }
    
        if (node.right != null) {
            prettyPrintTree(node.right, prefix + (isLeft ? "│   " : "    "), false);
        }
    
        System.out.println(prefix + (isLeft ? "└── " : "┌── ") + "[" + node.getA() + "," + node.getB() + "]");
    
        if (node.left != null) {
            prettyPrintTree(node.left, prefix + (isLeft ? "    " : "│   "), true);
        }
    }
    
    public static void prettyPrintTree(TreeNode node) {
        prettyPrintTree(node,  "", true);
    }

    public static void main(String[] args) throws Exception
    {
        ArrayList<Pair> nodes = new ArrayList<>();
        
        // [(1, 4), (8, 5), (3, 6), (10, -1), (4, 7)]
        // [(1, 6), (3, 7), (2, 4)]
        
        // nodes.add(new Pair(1,4));
        // nodes.add(new Pair(8,5));
        // nodes.add(new Pair(3,6));
        // nodes.add(new Pair(10,-1));
        // nodes.add(new Pair(4,7));

        nodes.add(new Pair(2, 4));
        nodes.add(new Pair(1, 6));
        nodes.add(new Pair(3, 7));

        Collections.sort(nodes, new Compare());

        TreeNode head = algorithm(nodes, 0, nodes.size()-1);
        prettyPrintTree(head);
    }
}