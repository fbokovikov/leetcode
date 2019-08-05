class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        is_negative = x < 0;
        str_x = str(x)
        """use for fast string concatenation"""
        digits_list = []
        ignore_zeros = True
        for c in reversed(str_x):
            if c == '-':
                continue
            if c == '0' and ignore_zeros:
                continue
            ignore_zeros = False
            digits_list.append(c);

        reversed_x = 0 if not digits_list else int(''.join(digits_list))
        if reversed_x > (2 ** 31 - 1) or x < - 2 ** 31:
            reversed_x = 0
        return -reversed_x if is_negative else reversed_x

    def isPalindrome(x: int) -> bool:
        str_x = str(x)
        index = 0
        len_x = len(str_x)
        while index < len(str_x) / 2:
            if str_x[index] != str_x[len_x - index - 1]:
                return False
            index += 1
        return True


def main():
    x = int(input("Введите число: "))
    """reversed_x = Solution.reverse(x)"""
    """print("Reversed x:", reversed_x)"""
    print("Is palindrome:", Solution.isPalindrome(x))

    string = "qwerty"
    """string[a:b:c] = a - startPosition, b - endPosition, c - stepSize"""


if __name__ == '__main__':
    main()
