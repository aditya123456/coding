import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_p = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(100, min(1000, sqrt_n + 1)):
        for j in range(i, min(1000, n // i + 1)):
            prod = i * j
            # print(prod)
            if prod > n:
                break
            converstr = str(prod)
            # print(converstr)
            # print(converstr[::-1])
            if str(prod) == converstr[::-1] and prod > max_p and prod < n:
                max_p = prod
    print(max_p)
