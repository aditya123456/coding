import re


text_to_search = '''
abcdefghijklmnopqrst
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

ha haha
MetaCharacter (Need to be scaped):
. ^ $ % & * ( ) [ ]  { } +

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900.555.1234
Mr. Aditya
Mr. Ram
Mr.Vishal
Mr T
Mrs. Rss
'''
# literal match
pattern = re.compile(r'abc')
matches  = pattern.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())


pattern1 = re.compile(r'\bha')
matches  = pattern1.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())


pattern2 = re.compile(r'\Bha')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())


pattern2 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())

pattern2 = re.compile(r'[8-9]00[-.]\d\d\d[-.]\d\d\d\d')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())

pattern2 = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())

pattern2 = re.compile(r'Mr\.?\s[A-Z]\w*')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())

pattern3 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches  = pattern2.finditer(text_to_search)
print(matches)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.span())

import re


def validate_password(password):
    # Positive Lookahead: At least 8 characters long and contains at least one uppercase letter and one digit
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$')

    # Negative Lookahead: Does not contain the sequence 'password'
    pattern_no_password = re.compile(r'^(?!.*password).*$')

    if pattern.match(password) and pattern_no_password.match(password):
        return True
    else:
        return False


# Test the function
password1 = "123Ab@gggg"  # Valid password
password2 = "WeakPass"  # Invalid (less than 8 characters)
password3 = "NoDigitsHere"  # Invalid (no digits)
password4 = "password123"  # Invalid (contains the sequence 'password')

print("Password 1:", validate_password(password1))  # Output: True
print("Password 2:", validate_password(password2))  # Output: False
print("Password 3:", validate_password(password3))  # Output: False
print("Password 4:", validate_password(password4))  # Output: False




