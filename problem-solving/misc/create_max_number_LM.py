


def createNumber(nums):
    nums = [str(num) for num in nums]
    nums.sort(reverse=True, key=lambda x: x * 3)  # Using x*3 for numbers with more than one digit
    return ''.join(nums)

numbers_array = [3, 30, 34, 5, 9]
max_number = createNumber(numbers_array)
print(max_number)
