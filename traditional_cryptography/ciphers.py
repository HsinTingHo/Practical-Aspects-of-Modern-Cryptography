
char = [
  'A', 'B', 'C', 'D', 'E',
  'F', 'G', 'H', 'I', 'J',
  'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T',
  'U', 'V', 'W', 'X', 'Y', 'Z'
]

#affine cipher: f(n) = (an+b) mod m
def affine_encoding(a, b, n, m):
  index = (a*n+b)%m
  print('Original char:', char[n])
  print('Index:', index,'Char: ', char[index])
  return char[index]

#caesar cipher: f(n) = (n+3) mod m
def caesar_encoding(n,m):
  index = (n+3)%m
  print('Original char:', char[n])
  print('Index:', index,'Char: ', char[index])
  return char[index]

def caesar_decoding(n,m):
  index = n%m-3
  print('Encoded char:', char[n])
  print('Index:', index,'Char: ', char[index])
  return char[index]