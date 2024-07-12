
A = [3, 5, 2, 19, 10, 4, 20]
m =3

def diffsum(A, M):

    sorted_array = sorted(A)
    print(sorted_array)
    print(sorted_array[-M:])
    max_sum = sum(sorted_array[-M:])
    min_sum = sum(sorted_array[1:M])
    result = max_sum - min_sum
    return result

print(diffsum([5, 8, 3, 8, 2, 1,9], 3))

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Write your code here
    missingnumber = []
    for i in range(10):
        if str(i) not in s:
            missingnumber.append(str(i))
    missing_chars = []
    for char in range(ord('a'), ord('z') + 1):
        if chr(char) not in s:
            missing_chars.append(chr(char))
    final_list = missingnumber + missing_chars
    print(final_list)
    s1 = ''.join(final_list)
    return s1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
