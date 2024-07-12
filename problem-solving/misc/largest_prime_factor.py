#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    prime_factors = []
    n = int(input().strip())
    max_prime = -1

    # Divide n by 2 until it becomes odd
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Check for odd factors starting from 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        max_prime = n
    print(max_prime)

