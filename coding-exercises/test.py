def rotationalCipher(input, rotation_factor):

  cipher = []
  ascii_A = 65
  ascii_a = 97
  ascii_0 = 48
  for c in input:
    ascii = ord(c)
    rotated = c
    if ascii >=  ascii_A and ascii <= 90: 
      rotated = (ascii - ascii_A + rotation_factor) % 26 + ascii_A
    if ascii >=ascii_a and ascii <= 122:
      rotated = (ascii - ascii_a + rotation_factor) % 26 + ascii_a
    if ascii >=ascii_0 and ascii <= 57:
      rotated = (ascii - ascii_0 + rotation_factor) % 10 + ascii_0
    cipher.append(chr(rotated))
        
  return "".join(cipher)

print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
