# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution617:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(r1,r2):
            if r1 == None:
                return r2
            if r2 == None:
                return r1
            r1.val += r2.val
            r1.left = dfs(r1.left,r2.left)
            r1.right = dfs(r1.right,r2.right)
            return r1
        return dfs(t1,t2)