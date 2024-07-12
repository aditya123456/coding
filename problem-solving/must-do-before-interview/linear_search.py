

def LinearSearch(A, l, h, key):
    if h<l:
        return 'NOT_FOUND'
    if A[l]==key:
        return l
    return LinearSearch(A, l+1, h, key)

print(LinearSearch([3, 5, 6, 8, 9, 10], 0, 6, 5))