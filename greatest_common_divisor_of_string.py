


str1 = "AAAAAAA"
str2 = "A"


def gcd2(str1, str2):
    if len(str2) == 0 or len(str1) == 0:
        return ""
    substrings = []
    i =0
    j = len(str2)
    while i <= len(str1):
        print(i)
        substrings.append(str1[i:i+len(str2)])
        i = i + len(str2)
        if i > len(str1)-1:
            break
    if all([i == str2 for i in substrings]):
        print(substrings)
        return str2
    else:
        j = j - 1
        str2 = str2[:j]
        print(str2)
        gcd(str1, str2)

    # print(substrings)
#
# x = gcd(str1, str2)
# print(x)


from math import gcd
def gcd1(str1, str2):
    if str1+str2 != str2+str1:
        return ""

    return str1[:gcd(len(str1), len(str2))]

print(gcd1(str1, str2))



def gcdString(str1, str2):
    pass
