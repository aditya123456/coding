nums = [-1,0,1,2,-1,-4]
result=set()
nums.sort()

n = len(nums)

for i in range(n-2):
    j = i + 1
    k = n-1
    while j < k:
        tmp = nums[i] + nums[j] + nums[k]

        if tmp == 0:
            result.add((nums[i], nums[j], nums[k]))
            j = j + 1
        elif tmp > 0:
            k = k - 1
        else:
            j = j +1
print(result)

