

def selectiosort(a):

    for i in range(len(a)):
        minindex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minindex]:
                minindex = j

        temp = a[i]
        a[i] = a[minindex]
        a[minindex] = temp
    return a

print(selectiosort([2, 5, 6, 1, 3]))

