

def PolyNomialMultiplication(a, b, n):
    product = [0 for i in range(2*n-1)]

    for i in range(n-1):
        for j in range(n-1):
            product[i+j] = product[i+j]+a[i]*b[j]
    return product

print(PolyNomialMultiplication([3,4,5], [3,4,5], 3))


def PolyNomialMultiplicationDivide(a, b, n, ac, bc):
    product = [0 for i in range(2*n-1)]

    if n == 1:
        product[0] = a[ac]*b[bc]

    for i in range(n-2):
        product[i] = PolyNomialMultiplicationDivide(a, b, n/2, a[i], b[i])
    for i in range(n, 2*n-2):
        product[i] = PolyNomialMultiplicationDivide(a, b, n/2, a[i]+n/2, b[i]+n/2)
    d0e1 = PolyNomialMultiplicationDivide(a, b, n/2, ac+n/2, bc)
    d2e0 = PolyNomialMultiplicationDivide(a, b, n / 2, ac, bc+n/2)
    for i in range(0, n+n/2-2):
        product[i] = d0e1 + d2e0
    return product
