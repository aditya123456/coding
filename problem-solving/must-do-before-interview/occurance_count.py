
A = [2, 2, 2, 3, 3, 4, 5, 6, 6]
M=4


def countdigit(A, M, N):

    digitdict = {}
    result = 0

    for i in range( N):
        if A[i] in digitdict:
            digitdict[A[i]] = digitdict[A[i]] + 1
        else:
            digitdict[A[i]] = 1
    print(digitdict)
    for k in digitdict.values():
        if k != M:
            result = result + M -k
    return  result

print(countdigit([2,2, 2, 3, 4, 4, 8, 9], 4, 8))