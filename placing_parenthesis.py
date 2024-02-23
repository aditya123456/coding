def max_parenthesis_placement(expression):
    n = len(expression)
    nums = []
    ops = []

    # Separate numbers and operators
    i = 0
    while i < n:
        if expression[i].isdigit():
            num = int(expression[i])
            while i + 1 < n and expression[i + 1].isdigit():
                num = num * 10 + int(expression[i + 1])
                i += 1
            nums.append(num)
        else:
            ops.append(expression[i])
        i += 1

    m = len(nums)
    dp_max = [[0] * m for _ in range(m)]
    dp_min = [[0] * m for _ in range(m)]

    for i in range(m):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    for length in range(2, m + 1):
        for i in range(m - length + 1):
            j = i + length - 1
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                elif ops[k] == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
                elif ops[k] == '*':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] * dp_max[k + 1][j], dp_min[i][k] * dp_max[k + 1][j], dp_max[i][k] * dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] * dp_min[k + 1][j], dp_max[i][k] * dp_min[k + 1][j], dp_min[i][k] * dp_max[k + 1][j])
                elif ops[k] == '/':
                    if dp_min[k + 1][j] != 0:
                        dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] / dp_min[k + 1][j])
                        dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] / dp_max[k + 1][j])
    print(dp_max)
    print(dp_min)
    return dp_max[0][m - 1]

# Example usage:
expression = "1+2*3-4/2"
result = max_parenthesis_placement(expression)
print(result)
