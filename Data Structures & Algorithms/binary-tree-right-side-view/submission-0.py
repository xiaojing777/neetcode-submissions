# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        
        result = []

        while q:
            level_size = len(q)
            for i in range(level_size):
                cur = q.popleft()
                if i==level_size-1:
                    result.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        
        return result


        

        