
import math
def BinarySearch(A, l, h, key):
    if h<l:
        return l-1
    mid = math.floor((l+h)/2)
    print(mid)
    if A[mid]==key:
        return mid
    elif A[mid] > key:
        return BinarySearch(A, l, mid-1, key)
    else:
        return BinarySearch(A, mid+1, h, key)

print(BinarySearch([3, 5, 6, 8, 9, 10], 1, 6, 8))