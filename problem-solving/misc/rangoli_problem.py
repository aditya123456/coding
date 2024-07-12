def print_rangoli(size):
    import string

    if size < 1 or size > 26:
        print("Invalid size. Size should be between 1 and 26.")
        return

    letters = string.ascii_lowercase[:size]

    # Generating the top half of the rangoli
    for i in range(size - 1, 0, -1):
        row = '-'.join(letters[i-1::-1] + letters[i:])
        print((row).center(size * 4 - 3, '-'))

    # Generating the bottom half of the rangoli
    for i in range(size):
        row = '-'.join(letters[i:size][::-1] + letters[i:size][1:])
        print((row).center(size * 4 - 3, '-'))

# Example usage
size = 4
print_rangoli(size)
