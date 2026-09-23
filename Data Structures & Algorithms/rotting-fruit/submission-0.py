import collections

directions = [[1,0], [-1,0], [0,1], [0,-1]]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        R = len(grid)
        C = len(grid[0])
        q = collections.deque()
        minute = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
        
        while q and fresh>0:
            level_size = len(q)
            for _ in range(level_size):
                cur_x,cur_y = q.popleft()
                for dx,dy in directions:
                    next_x,next_y = cur_x+dx,cur_y+dy
                    if next_x<0 or next_x>=R or next_y<0 or next_y>=C:
                        continue
                    if grid[next_x][next_y]==1:
                        fresh -= 1
                        grid[next_x][next_y] = 2
                        q.append([next_x, next_y])
            minute += 1
        
        if fresh!=0:
            return -1
        else:
            return minute
                


        