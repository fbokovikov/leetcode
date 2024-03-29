def longestCommonSubstring(self, s1: str, s2: str) -> str:
    n = len(s1)
    m = len(s2)

    lc_suff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_length = 0

    row = 0
    col = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lc_suff[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                lc_suff[i][j] = lc_suff[i - 1][j - 1] + 1
                if max_length < lc_suff[i][j]:
                    max_length = lc_suff[i][j]
                    row = i
                    col = j
            else:
                lc_suff[i][j] = 0

    result = [None] * max_length
    while lc_suff[row][col] > 0:
        result_index = lc_suff[row][col] - 1
        result[result_index] = s1[row - 1]
        col -= 1
        row -= 1
    return "".join(result)
