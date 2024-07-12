def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    # Initialize an array to store the length of the LIS ending at each index
    dp = [1] * len(nums)

    # Iterate over all elements in the array
    for i in range(1, len(nums)):
        # Check for increasing subsequence ending at index i
        for j in range(i):
            print(i, j)
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp represents the length of the longest increasing subsequence
    print(dp)
    return max(dp)

# Example usage:
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(nums)

print(f"Length of the Longest Increasing Subsequence: {result}")
