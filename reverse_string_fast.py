def find_palindromes(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right + 1])
            left -= 1
            right += 1

    palindromes = []
    for i in range(len(s)):
        expand_around_center(i, i)  # Odd length palindromes
        expand_around_center(i, i + 1)  # Even length palindromes

    return palindromes

input_string = "abcbamadamhellohannah"
all_palindromes = find_palindromes(input_string)
print(all_palindromes)



def reverse_string(string):
    string_list = list(string)  # Convert the string to a list for in-place manipulation
    left = 0  # Pointer for the left end of the string
    right = len(string_list) - 1  # Pointer for the right end of the string

    while left < right:
        # Swap characters at left and right pointers
        string_list[left], string_list[right] = string_list[right], string_list[left]
        # Move pointers inward
        left += 1
        right -= 1

    return ''.join(string_list)  # Convert the list back to a string

string_to_reverse = "hello" * 20000  # Example 100,000 character long string
reversed_string = reverse_string(string_to_reverse)
print(reversed_string[:20])  # Output: "olleholleholleholleh"
