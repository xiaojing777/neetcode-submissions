# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if root is None:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height == -1 or right_height== -1:
            return -1
        elif abs(left_height - right_height)>1:
            return -1
        else:
            return max(left_height, right_height)+1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if self.getHeight(root)==-1:
            return False
        else:
            return True

        
        