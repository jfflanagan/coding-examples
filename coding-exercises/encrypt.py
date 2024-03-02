def encrypt(s, l, r):
  if r == l:
    return s[l]
  if l > r:
      return ""
  
  mid  = (r - l) // 2 + l
  encrypted = s[mid]

  encrypted += encrypt(s, l, mid - 1)
  encrypted += encrypt(s, mid + 1, r)
  
  return encrypted
  
def findEncryptedWord(s):

  return encrypt(s, 0, len(s) - 1)

print(findEncryptedWord("abcd"))