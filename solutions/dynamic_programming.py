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

    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        n = len(s)
        decodings = [0] * (n + 1)
        decodings[0] = 1
        decodings[1] = 1 if int(s[0]) > 0 else 0
        for i in range(2, n + 1):
            first = int(s[i - 1])
            if first > 0:
                decodings[i] = decodings[i - 1]
            second = int(s[i - 2:i])
            if 10 <= second <= 26:
                decodings[i] += decodings[i - 2]
        return decodings[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost) == 0:
            return 0
        n = len(cost)
        res = [0] * n
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, n):
            res[i] = min(res[i - 1], res[i - 2]) + cost[i]
        return min(res[n - 1], res[n - 2])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pass

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [0] * n
        for i in range(1, min(nums[0] + 1, n)):
            jumps[i] = 1
        for i in range(1, n):
            prev_jump = nums[i - 1]
            for j in range(i + prev_jump, min(i + nums[i] + 1, n)):
                if jumps[j] == 0:
                    jumps[j] = jumps[i] + 1
                else:
                    jumps[j] = min(jumps[j], jumps[i] + 1)
        return jumps[n - 1]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_position = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] >= last_position - i:
                last_position = i
        return last_position == 0

    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0
        n = len(height)
        total_water, cur_water = 0, 0
        cur_height = height[0]
        for i in range(0, n):
            if height[i] < cur_height:
                cur_water += cur_height - height[i]
            else:
                total_water += cur_water
                cur_water = 0
                cur_height = height[i]
            if i == n - 1:
                min_height = min(cur_height, height[n - 1])
                while height[i] != cur_height:
                    if height[i] < min_height:
                        total_water += min_height - height[i]
                    else:
                        min_height = height[i]
                    i -= 1
        return total_water

    def longestValidParentheses(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        valids = [0] * n
        for i in range(1, n):
            if s[i] == '(':
                continue
            if s[i - 1] == '(':
                valids[i] = 2
                if i >= 2:
                    valids[i] += valids[i - 2]
            if s[i - 1] == ')':
                prev_length = valids[i - 1]
                if prev_length > 0 and i - prev_length > 0:
                    if s[i - prev_length - 1] == '(':
                        valids[i] = 2 + prev_length + valids[i - prev_length - 2]
        return max(valids)

    def isMatch(self, s: str, p: str) -> bool:
        """
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        """
        def is_match(self, text, pattern):
            if not pattern:
                return not text

            first_match = bool(text) and pattern[0] in {text[0], '.'}

            if len(pattern) >= 2 and pattern[1] == '*':
                return (self.isMatch(text, pattern[2:]) or
                        first_match and self.isMatch(text[1:], pattern))
            else:
                return first_match and self.isMatch(text[1:], pattern[1:])

        def isMatch(self, text, pattern):
            memo = {}

            def dp(i, j):
                if (i, j) not in memo:
                    if j == len(pattern):
                        ans = i == len(text)
                    else:
                        first_match = i < len(text) and pattern[j] in {text[i], '.'}
                        if j + 1 < len(pattern) and pattern[j + 1] == '*':
                            ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                        else:
                            ans = first_match and dp(i + 1, j + 1)

                    memo[i, j] = ans
                return memo[i, j]

            return dp(0, 0)

        def minDistance(self, word1: str, word2: str) -> int:
            pass

def main():
    triangle = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    s = "()))()()))((()))"
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    print(sol.longestValidParentheses(s))


if __name__ == '__main__':
    main()
