

def joesephus(n, k):
    rebels = list(range(0, n+1))
    index = 0
    while len(rebels) > 1:
        index = (index + k-1) % len(rebels)
        eleminated_person = rebels.pop(index)
        print(index, rebels)
    return rebels

print(joesephus(12, 3))


