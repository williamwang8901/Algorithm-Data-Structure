public class Binary_Tree_Longest_Consecutive_Sequence_298 {
	class TreeNode {
	      int val;
	      TreeNode left;
	      TreeNode right;
	      TreeNode(int x) { val = x; }
	}
    public int longestConsecutive(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        return find(root, 0, root.val - 1);
    }
    
    public int find(TreeNode root, int length, int prev) {
        if (root == null) {
            return length;
        }
        
        int currentLen = root.val == prev + 1 ? length + 1 :  1;
        
        return Math.max(currentLen , Math.max(find(root.left, currentLen, root.val), find(root.right, currentLen, root.val)));
    }
}