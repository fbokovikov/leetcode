from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr_sum: int, cur_list:  List[int], main_list:  List[int]) -> None:
            for i in range(len(main_list)):
                if curr_sum + main_list[i] == target:
                    solution.append(cur_list + [main_list[i]])
                    return
                if curr_sum + main_list[i] > target:
                    return
                else:
                    backtrack(curr_sum + main_list[i], cur_list + [main_list[i]], main_list[i:])

        solution = []
        backtrack(0, [], sorted(candidates))

        return solution

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, cur_combination, cur_sum, target, start) -> None:
            if cur_sum > target:
                return
            elif cur_sum == target:
                result.append(list(cur_combination))
            else:
                for idx in range(start, len(candidates)):
                    if idx > start and candidates[idx] == candidates[idx - 1]:
                        continue
                    val = candidates[idx]
                    backtrack(candidates, cur_combination + [val], cur_sum + val, target, idx + 1)
        result = []
        backtrack(sorted(candidates), [], 0, target, 0)
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sequence: str, n: int, left_count: int, right_count: int, solution: List[str]):
            if right_count > left_count:
                return
            if n == 0:
                if right_count == left_count:
                    solution.append(sequence)
            else:
                backtrack(sequence + "(", n - 1, left_count + 1, right_count, solution)
                backtrack(sequence + ")", n - 1, left_count, right_count + 1, solution)

        solution = []
        backtrack("", n * 2, 0, 0, solution)
        return solution

    def letterCombinations(self, digits: str) -> List[str]:

        digits_dict = {
            "1": {},
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def _letterCombinations(digits: str) -> List[str]:
            if len(digits) == 0:
                return []
            possible_digits = digits_dict.get(digits[0])
            if len(digits) == 1:
                return possible_digits
            else:
                res = []
                for idx in range(len(possible_digits)):
                    res += [possible_digits[idx] + comb for comb in _letterCombinations(digits[1:])]
            return res

        return _letterCombinations(digits)


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sol = Solution()
    print(sol.combinationSum2(candidates, target))

    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(sol.combinationSum2(candidates, target))


if __name__ == '__main__':
    main()
