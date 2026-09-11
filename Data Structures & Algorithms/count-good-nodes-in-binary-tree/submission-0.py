# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur, maxVal):
            if cur is None:
                return 0
            if cur.val>=maxVal:
                result = 1
            else:
                result = 0
            
            maxVal = max(cur.val, maxVal)

            result = result + dfs(cur.left, maxVal) + dfs(cur.right, maxVal)

            return result
        
        return dfs(root, root.val)
        