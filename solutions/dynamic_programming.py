class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [None] * (n + 2)
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]


def main():
    sol = Solution()
    print(sol.climbStairs(1))


if __name__ == '__main__':
    main()
