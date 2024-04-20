'''
1. Maximum difference between 2 numbers in a list
The question had a list as an input ([3, 6, 10, 1, 4, 6, 5], for example)
You have to design an algorithm that finds the greatest difference between two elements, such that the larger element appears after the smaller element.
In the example above, the output should be 7 (10-3 = 7).

Return -1 if the maximum difference is flat or negative.

Constraints I remember:
1 =< size of array


2. The size of the longest increasing subsequence
Given an array like {1,1,3,2,6,4,1,7}, find the longest increasing subsequence. In this case it is 4, {1, 3, 6, 7}.

If there is no increasing subsequence, return 1. E.g. arr = {5,3,1}, return 1.

'''


def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    lis = [1] * n
    sequence = []

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
                sequence.append(nums[i])
    print(sequence)

    return max(lis) if max(lis) > 1 else 1
l = [1,1,3,2,6,4,1,7]
x = longest_increasing_subsequence(l)
print(x)




def max_diff(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_index = i
    min_arr = float('inf')
    min_tmp = arr[:max_index]
    print(min(min_tmp))
    for j in range(len(arr[:max_index])):
        if arr[j] < min_arr and arr[j] > 0:
            min_arr = arr[j]

    print(max)
    print(min_arr)
    print(max-min_arr)

def max_diff_2(arr):
    min_diff = arr[0]
    max_diff = 0

    for num in arr[1:]:
        max_diff = max(max_diff, num-min_diff)
        min_diff = min(num, min_diff)
    print(max_diff)


# mx = [-3, -6, 10, -1, -4, 76, 577]
# max_diff(mx)
# max_diff_2(mx)

