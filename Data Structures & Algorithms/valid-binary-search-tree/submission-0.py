# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if not self.isValidBST(root.left):
            return False

        if self.pre and root.val<=self.pre.val:
            return False
        self.pre = root

        if not self.isValidBST(root.right):
            return False

        return True
        