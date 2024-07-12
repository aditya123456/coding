


def max_sum(arr):
    max_s = float('-inf')

    for i in range(len(arr)-1):
        temp = 0
        for j in range(i+1, len(arr)):
            # print(arr[j])
            temp = temp + arr[j]
        # print(temp)
        if temp > max_s:
            max_s = temp
        # print(max_s)
    print(max_s)

arr = [1, 4, 3, 5, 2, 4]
max_sum(arr)