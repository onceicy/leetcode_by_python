# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution226:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = [root]
        while queue:
            tmp = queue.pop(0)
            tmp.left,tmp.right = tmp.right,tmp.left
            if tmp.left:
                queue.append(tmp.left)	
            if tmp.right:
                queue.append(tmp.right)
        return root