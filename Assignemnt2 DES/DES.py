#reference: https://github.com/Hamza-Megahed/des-calculator
import public_tables as pt

tables = pt.public_tables()
IP_table = tables.IP_table
PC1_table = tables.PC1_table
PC2_table = tables.PC2_table
E_table = tables.E_table
S_table = tables.S_tables
P_table = tables.P_table

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
    #print('cd1', c1+d1)
    return PC2(table, len(table), c1+d1),c1,d1 #48 bits, 28 bits, 28 bits

def expansion(table, src_width, src):
    return permute(table, src_width, src)

def f(r_msg, key):
    expanded_r = expansion(E_table, len(E_table), r_msg) #r is expanded from 32 bits to 48 bits
    bin_r_msg = int(expanded_r, 2)
    bin_key = int(key, 2)
    xor = bin(bin_r_msg^bin_key)[2:].zfill(48)
    #divide into 8 segment and pass each segment to s_box according to order
    after_s = ''

    for i in range(8):
        after_s += s_box(S_table[i], xor[i*6:(i+1)*6])
    return permute(P_table, len(P_table), after_s)

def s_box(table, six_b_key):
    #convert [1:5] to decimal -> pick up column
    #convert[0] U [5] to decimal -> pick up row
    column = int(six_b_key[1:5],2)
    row = int(six_b_key[0]+six_b_key[-1], 2)
    index = 16*row+column
    return bin(table[index])[2:].zfill(4)

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
