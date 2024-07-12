def needleman_wunsch(str1, str2, match=1, mismatch=-1, gap=-2):
    n = len(str1) + 1
    m = len(str2) + 1

    # Initialize the matrix
    dp = [[0] * m for _ in range(n)]

    # Initialization
    for i in range(n):
        dp[i][0] = i * gap
    for j in range(m):
        dp[0][j] = j * gap

    # Matrix filling
    for i in range(1, n):
        for j in range(1, m):
            match_mismatch = dp[i - 1][j - 1] + (match if str1[i - 1] == str2[j - 1] else mismatch)
            gap_first_str = dp[i - 1][j] + gap
            gap_second_str = dp[i][j - 1] + gap
            dp[i][j] = max(match_mismatch, gap_first_str, gap_second_str)

    # Backtracking to find the alignment
    align1, align2 = '', ''
    i, j = n - 1, m - 1
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            align1 = str1[i - 1] + align1
            align2 = '-' + align2
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + gap:
            align1 = '-' + align1
            align2 = str2[j - 1] + align2
            j -= 1
        else:
            align1 = str1[i - 1] + align1
            align2 = str2[j - 1] + align2
            i -= 1
            j -= 1

    return align1, align2

# Example usage:
str1 = "AGTACGCA"
str2 = "TATGC"
alignment1, alignment2 = needleman_wunsch(str1, str2)

print("Optimal Alignment:")
print(alignment1)
print(alignment2)
