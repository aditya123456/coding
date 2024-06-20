


class Revision:


    def longest_pallindrom(self):
        string = "acddcad"
        def expand(i, j):
            while i >=0 and j < len(string) and string[i] == string[j]:
                i = i - 1
                j = j + 1
            return string[i+1:j]
        ans = ''
        for i in range(len(string)):
            ans = max(ans, expand(i, i), expand(i, i + 1), key=len)
        print(ans)

    def largest_increasing_subsequence(self):
        pass

cl = Revision()
cl.longest_pallindrom()