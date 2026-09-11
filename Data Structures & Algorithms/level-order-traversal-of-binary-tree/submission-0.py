# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            level_size = len(q)
            level_result = []
            for _ in range(level_size):
                cur = q.popleft()
                level_result.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(level_result)

        return result
                

        