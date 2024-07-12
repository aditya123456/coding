

def pointCover(n, ar):
    segment = []
    left = 1
    while left<=n:
        (l, r) = (ar[left], ar[left]+2)
        segment.append((l, r))
        left = left + 1
        while left<=n and ar[left]<=r:
            left = left + 1
    return segment


print(pointCover(5, [1, 2, 3, 4, 5, 6]))