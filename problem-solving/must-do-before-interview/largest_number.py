
def largest(ar):

    index = 0
    largest = None
    numbers = []
    while len(ar) > 1:
        max = 0
        for i in range(len(ar)):
            if ar[i] >= max:
                max = ar[i]
                index = i
        ar.pop(index)
        print(ar)
        numbers.append(max)
    numbers.append(ar[0])
    return ''.join(map(str, numbers))

print(largest([9, 3,4, 9,3]))