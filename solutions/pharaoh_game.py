from typing import List


class Solution():
    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "**": lambda x, y: x ** y
        }


    def execute(self, operation: str, x: int, y: int):
        return self.operations[operation](x, y)

    def operation_comb(self) -> List[List[str]]:
        res = []
        def helper(cur_path):
            if len(cur_path) == 3:
                res.append(cur_path)
                return
            else:
                for op in self.operations.keys():
                    helper(list(cur_path) + [op])
        helper([])
        return res

    def combinations(self, n: int) -> List[str]:
        result = []
        dices = [1] * 4
        possible_ops = self.operation_comb()
        for idx in range(0, 6 ** 5):
            dices[3] = idx % 6 + 1
            dices[2] = idx % (6 ** 2) // 6 + 1
            dices[1] = idx % (6 ** 3) // (6 ** 2) + 1
            dices[0] = idx // (6 ** 4) + 1
            for ops in possible_ops:
                res = self.operations[ops[0]] (dices[3], dices[2])
                res = self.operations[ops[1]] (res, dices[1])
                res = self.operations[ops[2]] (res, dices[0])
                if res == n:
                    result.append(str(dices[3]) + ops[0] + str(dices[2]) + ops[1]
                                  + str(dices[1]) + ops[2] + str(dices[0]))
        return result

def main():
    sol = Solution()
    print(sol.combinations(4))



if __name__ == '__main__':
    main()