def compress(s):
    result = ""
    i = 0

    while (i <= len(s)-1):
        count = 1
        while (i < len(s)-1) and (s[i] == s[i+1]):
            i += 1
            count += 1
        result += s[i] + str(count)
        i += 1
    return result


def compress2(s):
    result = ""
    i = 0

    while (i <= len(s)-2):
        chars = s[i]
        count = s[i+1]
        while (i < len(s)-2) and (s[i+1] == s[i+3]):
            i += 2
            chars += s[i]
        result += chars + count
        i += 2
    return result


def decompress2(s):
    result = ""
    i = 0

    while (i <= len(s)-1):
        if s[i].isalpha():
            if i+1 < len(s) and s[i+1].isalpha():
                result += s[i] + s[i+2]
            else:
                result += s[i]
        else:
            result += s[i]
        i += 1
    return result


def decompress(s):
    result = ""
    i = 0

    while (i <= len(s)-2):
        result += s[i] * int(s[i+1])
        i += 2
    return result


# Test the functions
s = 'aabbcaaaccc'
s1 = compress(s)
s2 = compress2(s1)
s3 = decompress2(s2)
s4 = decompress(s3)

'''
print(f'Original string: {s}')
print(f'After compress: {s1}')
print(f'After compress2: {s2}')
print(f'After decompress2: {s3}')
print(f'After decompress: {s4}')
'''

# Test Case 1: Basic Case
input_str1 = 'aabbcaaaccc'
expected_output1 = 'a2b2c1a3c3'

# Test Case 2: Single Character
input_str2 = 'aaaa'
expected_output2 = 'a4'

# Test Case 3: Mixed Characters
input_str3 = 'abccdd'
expected_output3 = 'a1b1c2d2'

# Test Case 4: Empty String
input_str4 = ''
expected_output4 = ''

# Test Case 5: Complex Case
input_str5 = 'xyyzzaaaabbbb'
expected_output5 = 'x1y1z2a4b4'

# Test Case 6: Characters and Numbers
input_str6 = 'a3b2c1d4'
expected_output6 = 'aaaabbdddd'

# Test Case 7: Special Characters
input_str7 = '!@#$%^'
expected_output7 = '!1@1#1$1%1^1'

# Test Case 8: Random Characters
input_str8 = 'abcdefg'
expected_output8 = 'a1b1c1d1e1f1g1'

# Test Case 9: Large Repetition
input_str9 = 'aaaabbbbcccccddddd'
expected_output9 = 'a4b4c5d5'

# Run the tests
test_cases = [
    (input_str1, expected_output1),
    (input_str2, expected_output2),
    (input_str3, expected_output3),
    (input_str4, expected_output4),
    (input_str5, expected_output5),
    (input_str6, expected_output6),
    (input_str7, expected_output7),
    (input_str8, expected_output8),
    (input_str9, expected_output9),
]

for input_str, expected_output in test_cases:
    compressed_str = compress(input_str)
    compress2_str = compress2(compressed_str)
    decompressed_str = decompress(compressed_str)
    print(f'Original string: {input_str}')
    print(f'After compress: {compressed_str}')
    print(f'After compress2: {compress2_str}')
    print(f'After decompress: {decompressed_str}')
    if decompressed_str == input_str:
        print("VERIFIED!!!")
    print('\n' + '-'*40 + '\n')
