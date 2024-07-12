


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r):
        if A[i] <= x:
            j= j+1
            temp = A[i]
            A[j] = A[i]
            A[i] = temp
    temp2 = A[l]
    A[l] = A[j]
    A[j] = temp2
    return j

def quickSort(A, l, r):
    if len(A) == 1:
        return A
    pivot = partition(A, l, r)
    quickSort(A, l, pivot-1)
    quickSort(A, pivot+1, r)
