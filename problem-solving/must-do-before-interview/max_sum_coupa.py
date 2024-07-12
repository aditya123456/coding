
A = [4, 10, 2, 13, 15, 4, 1, 20, 15]

def max_sum(A, N):
    result = 0
    for i in range( N):
        if i % 2 != 0:
            result = result + max(A)
            index = A.index(max(A))
            A.pop(index)
        else:
            result = result - min(A)
            index = A.index(min(A))
            A.pop(index)
    return result

print(max_sum([6, 8, 10, 4, 3, 1], 6))