def rotate(arr, n):
    last_el = arr[n - 2]

    for i in range(n - 2, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_el


# Driver function
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ')
