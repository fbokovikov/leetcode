class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        """
        Given a string, find the length of the longest substring without repeating characters.
        """
        char_dict = {}
        start = 0
        cur_pos = 0
        max_len = 0

        for c in s:
            if c in char_dict:
                start = max([char_dict.get(c) + 1, start])

            cur_len = cur_pos - start + 1

            if cur_len > max_len:
                max_len = cur_len

            char_dict[c] = cur_pos
            cur_pos += 1

        return max_len


def main():
    s = input("Введите строку: ")
    print(Solution.length_of_longest_substring(s))


if __name__ == "__main__":
    main()
