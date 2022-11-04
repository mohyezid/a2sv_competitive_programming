  r , c = len(grid),len(grid[0])
        if not grid:
            return
        for i in range(1,r):
            grid[i][0] += grid[i-1][0]
        for i in range(1,c):
            grid[0][i] += grid[0][i-1]
        for i in range(1,r):
            for j in range(1,c):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[r-1][c-1]
