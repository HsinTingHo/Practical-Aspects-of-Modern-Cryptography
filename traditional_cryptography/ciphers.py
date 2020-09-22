
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

#block transposition cipher
def block_transposition_encoding(permutation_list, org_text, num_char):

  length = len(org_text)
  #fill dummy char(X)
  to_fill = num_char - (length%num_char)
  text = org_text+'X'*to_fill
  #permutation_list = [3,5,1,2,4]
  #to use the element in permutation_list as index, we need to deduct them by 1
  permutation_list = [x-1 for x in permutation_list]
  encoded_text = ''
  p = 0
  print(text)
  while p < len(text):
    for i in range(5):
      code_index = p+permutation_list[i]
      encoded_text += text[code_index]
      print('Org:',text[p+i], 'Encoded:', text[code_index])
    p += 5
  return encoded_text
