# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q:
            return False
        elif p and q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)

        while q:
            cur = q.popleft()
            if self.isSameTree(cur, subRoot):
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return False

        