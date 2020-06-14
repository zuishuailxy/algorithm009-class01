class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 行 TS:O(MN) SC:(MN)
        nr = len(grid)
        if nr == 0: return 0
        # 列
        nc = len(grid[0])

        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_island += 1
                    self.dfs(grid, r, c)
        
        return num_island
    
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    
    # BFS
    nr = len(grid)
    if nr == 0: return 0
    nc = len(grid[0])

    num_island = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "1":
                num_island += 1
                grid[r][c] = "0"
                neighbors = collections.deque([(r, c)])
                while neighbors:
                    row, col = neighbors.popleft()
                    for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] = "1":
                            neighbors.append((x, y))
                            grid[x][y] = "0"
    
    return num_island




