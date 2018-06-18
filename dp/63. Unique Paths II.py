class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 1
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        #print m,n
        grid = [[-1 for i in range(n)] for j in range(m)]
        j = 0
        while j<n:
            if obstacleGrid[0][j]!=1:
                grid[0][j] =1
            else:
                while j<n:
                    grid[0][j] = 0
                    j+=1
            j+=1
        j=0
        while j<m:
            if obstacleGrid[j][0]!=1:
                grid[j][0] =1
            else:
                while j<m:
                    grid[j][0] = 0
                    j+=1
            j+=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] ==1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]
            
