input_string = "hello"

cipher_shift = 1
a_idx = ord('a')
encoded_string = []
for c in input_string:
    # 26 chars in english latin alphabet
    encoded_ascii = ((ord(c) - a_idx + cipher_shift) % 26) + a_idx
    encoded_string.append(chr(encoded_ascii))

print(''.join(encoded_string))