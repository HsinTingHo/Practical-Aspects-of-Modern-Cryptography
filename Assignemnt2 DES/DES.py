#reference: https://github.com/Hamza-Megahed/des-calculator
import public_tables as pt

def hex_to_bin(msg):
    return bin(int(msg,16))[2:].zfill(64)

#permute(list, int, string)
def permute(table, src_width, src):
    tb_length = len(table)
    result = [0]*tb_length
    for i, location in enumerate(table):
        result[i] = src[location-1] #table start from 1
    return ''.join(result)

def initial_permutation(table, src_width, src):
    result = permute(table, src_width, src)
    return result[:32], result[32:]

def PC1(table, src_width, src):
    result = permute(table, src_width, src)
    return result[:28], result[28:]

def PC2(table, src_width, src):
    result = permute(table, src_width, src)
    return result

def shifting_rules():
    shift_nums = [2]*16
    one_bit_round = [1,2,9,16]
    for elem in one_bit_round:
        shift_nums[elem-1] = 1
    return shift_nums

def rotate(shift_num, direction, key):
    if direction == 'left':
        key = key[shift_num:]+key[:shift_num]
    else:
        key = key[-shift_num:]+key[:-shift_num]
    return key

def transformation(table, shift_num, direction, c, d):
    c1 = rotate(shift_num, direction, c)
    d1 = rotate(shift_num, direction, d)
    print('cd1', c1+d1)
    return PC2(table, len(table), c1+d1),c1,d1 #48 bits, 28 bits, 28 bits

# key: 0123456789ABCDEF
# plain text: 789AB123456789AA
# cipher text: e7ab74f51fb2e8a4
def DES(msg, key):

    # Shrink key from 64 bits to 48 bits
    # perform initial permutation on msg and split msg into left half and right half
    # perform transformation on key and encrypt for 16 times
    #     transformation 56 bits key to 48 bits
    #     perform f on 48 bits key and right half of msg
    #     new_right = XOR the result with left half of msg
    #     new_left = right half
    # final permutation
    pass
