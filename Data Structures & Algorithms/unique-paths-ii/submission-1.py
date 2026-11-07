class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        dp[len(obstacleGrid)][len(obstacleGrid[0])-1] = 1
        for i in range(len(obstacleGrid)-1, -1, -1):
            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if(obstacleGrid[i][j] == 1): 
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]