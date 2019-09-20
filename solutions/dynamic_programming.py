from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum

    def climbStairs(self, n: int) -> int:
        steps = [None] * (n + 2)
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]

    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_robs = [0] * n
        max_robs[0] = nums[0]
        max_robs[1] = max(nums[0], nums[1])
        for i in range(2, n):
            max_robs[i] = max(nums[i] + max_robs[i - 2], max_robs[i - 1])
        return max_robs[n - 1]

    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        res = 0
        for price in prices:
            cur_min = min(price, cur_min)
            res = max(res, price - cur_min)
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        computed_paths = [[0] * n] * m
        for i in range(m):
            computed_paths[i][0] = 1
        for j in range(n):
            computed_paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                computed_paths[i][j] = computed_paths[i - 1][j] + computed_paths[i][j - 1]
        return computed_paths[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        computed_paths = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(0, n):
            if obstacleGrid[0][j] == 1:
                break
            computed_paths[0][j] = 1
        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                break
            computed_paths[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    computed_paths[i][j] = computed_paths[i - 1][j] + computed_paths[i][j - 1]
        return computed_paths[m - 1][n - 1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        M = len(grid)
        computed_paths = [[0] * N for _ in range(M)]
        computed_paths[0][0] = grid[0][0]
        for i in range(1, M):
            computed_paths[i][0] = computed_paths[i - 1][0] + grid[i][0]
        for j in range(1, N):
            computed_paths[0][j] = computed_paths[0][j - 1] + grid[0][j]
        for i in range(1, M):
            for j in range(1, N):
                computed_paths[i][j] = min(computed_paths[i - 1][j], computed_paths[i][j - 1]) + grid[i][j]
        return computed_paths[M - 1][N - 1]


def main():
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    sol = Solution()
    print(sol.minPathSum(grid))


if __name__ == '__main__':
    main()
