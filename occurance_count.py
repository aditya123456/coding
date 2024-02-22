


def countdigit(A, M, N):

    digitdict = {}
    result = 0

    for i in range( N):
        # for j in range(i+1, N):
        #     if A[i] == A[j]:
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