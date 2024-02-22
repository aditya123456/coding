


def diffsum(A, M):

    sorted_array = sorted(A)
    print(sorted_array)
    print(sorted_array[-M:])
    max_sum = sum(sorted_array[-M:])
    min_sum = sum(sorted_array[1:M])
    result = max_sum - min_sum
    return result

print(diffsum([5, 8, 3, 8, 2, 1,9], 3))
