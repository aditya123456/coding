

import math
def mergesort(a):
    if len(a) ==1:
        return a
    mid = math.floor(len(a)/2)

    c = [a[i] for i in range(mid)]
    d = [a[i] for i in range(mid, len(a))]
    k, l = 0, 0
    n = len(c)+len(d)
    print(d)
    e = [0 for i in range(n)]
    while len(c)!=0 and len(d)!=0:
        print(l)
        if c[k]<=d[l]:
            e[n] = d[l]
            k = k +1
            l = l+ 1
            n = n - 1
            d.pop(l)
        else:
            e[n] = c[l]
            k = k + 1
            l = l + 1
            n = n - 1
            c.pop(l)
    return d

print(mergesort([3, 6, 10, 1, 20, 4, 5,19]))

