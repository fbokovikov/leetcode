from typing import List, Set


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

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(cur_seq: List[int], res: List[List[int]], max):
            if len(cur_seq) == k:
                res.append(cur_seq)
            else:
                for i in range(max + 1, n + 1):
                    backtrack(cur_seq + [i], res, i)
        res = []
        for i in range(1, n - k + 2):
            backtrack([i], res, i)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur_path: List[int], start_pos, res):
            res.append(cur_path)
            for i in range(start_pos, len(nums)):
                backtrack(cur_path + [nums[i]], i + 1, res)
        res = []
        backtrack([], 0, res)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset: List[int], from_pos: int, res: List[List[int]]):
            res.append(subset)
            for i in range(from_pos, len(nums)):
                if i > from_pos and nums[i] == nums[i - 1]:
                    continue
                backtrack(subset + [nums[i]], i + 1, res)
        nums.sort()
        res = []
        backtrack([], 0, res)
        return res




def main():
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))


if __name__ == '__main__':
    main()
