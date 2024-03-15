class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        substrings = []

        for i in range(len(s)):
            substring = s[i]
            substrings.append(substring)
            for j in range(i + 1, len(s)):
                substring = substring + s[j]
                substrings.append(substring)
        print(substrings)
        pallindrom = []
        for j in range(len(substrings) - 1):
            maxstring = ''
            # print(substrings[j], substrings[j][::-1])
            if substrings[j] == substrings[j][::-1]:
                pallindrom.append(substrings[j])
        print(pallindrom)
        maxlen = []
        for i in range(len(pallindrom) - 1):
            if len(pallindrom[i]) > len(pallindrom[i + 1]):
                maxlen = pallindrom[i]
        return maxlen


#optimized
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ans = max(ans, self.expand(s, i, i), self.expand(s, i, i + 1), key=len)
        return ans


    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        print( s[i + 1:j])
        return s[i + 1:j]


s = Solution()
s.longestPalindrome("babad")