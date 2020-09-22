from traditional_cryptography import ciphers as c
char_table = {
  'A':0, 'B':1, 'C':2, 'D':3, 'E':4,
  'F':5, 'G':6, 'H':7, 'I':8 ,'J':9,
  'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
  'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,
  'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25
}
#test affine_encoding
test = 'STOPPOLLUTION'
length = len(test)
for i in range(length):
  num = char_table[test[i]]
  print(c.affine_encoding(17,22,num,26))

#test caesar_decoding
test = 'EOXHMHDQV'
length = len(test)
for i in range(length):
  num = char_table[test[i]]
  print(c.caesar_decoding(num,26))

#test block transposition cipher
test = 'GRIZZLYBEARS'
permutation_list = [3,5,1,2,4]
print(c.block_transposition_encoding(permutation_list, test, 5))