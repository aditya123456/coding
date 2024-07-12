class Solution:
    def convert(self, s: str, numRows: int) -> str:

        char_list = []
        row = 0
        i = 0
        while i != len(s):
            temp_char_list = []
            if row % 2 == 0:
                for j in range(numRows):
                    print(i)
                    temp_char_list.append(s[i])
                    i = i + 1
                    if i == len(s):
                        break
            else:
                print(i)
                temp_char_list.append(s[i])
                i = i + 1
            row = row + 1
            char_list.append(temp_char_list)
        print(char_list)
        sting_c = ''
        for i in range(len(char_list)):
            if i % 2 == 0:
                string_c = sting_c + char_list[i][1]
            else:
                if len(char_list[i]) > 0:
                    string_c = sting_c + char_list[i][1]
                else:
                    string_c = sting_c + char_list[i][0]
        print(string_c)


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)