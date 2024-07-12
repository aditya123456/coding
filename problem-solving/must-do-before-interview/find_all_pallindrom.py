

def find_palindromes(string):
    pall = []

    def expand(i, j):
        while i >0 and j<len(string) and string[i] == string[j]:
            pall.append(string[i:j+1])
            i = i -1
            j = j +1


    for i in range(len(string)):
        expand(i, i)
        expand(i, i+1)
    return pall



input_string = "abcbamadamhellohannah"
all_palindromes = find_palindromes(input_string)
print(all_palindromes)