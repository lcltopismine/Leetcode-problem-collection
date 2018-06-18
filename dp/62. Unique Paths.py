class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1 for i in range(n)] for j in range(m)]
        #print grid
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]
