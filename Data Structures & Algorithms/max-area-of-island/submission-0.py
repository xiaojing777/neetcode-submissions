directions = [[1,0], [-1,0], [0,1], [0,-1]]
count = 0

class Solution:
    def dfs(self, grid, visited, x, y):
        global count
        for dx,dy in directions:
            next_x, next_y = x+dx, y+dy
            if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                continue
            if grid[next_x][next_y]==1 and visited[next_x][next_y]==False:
                visited[next_x][next_y] = True
                count += 1
                self.dfs(grid, visited, next_x, next_y)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global count
        result = 0
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==False:
                    visited[i][j] = True
                    count = 1
                    self.dfs(grid, visited, i, j)
                    result = max(result, count)

        return result

        