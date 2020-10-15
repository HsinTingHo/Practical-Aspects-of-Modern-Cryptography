#reference: https://github.com/Hamza-Megahed/des-calculator
import public_tables as pt

tables = pt.public_tables()
IP_table = tables.IP_table
PC1_table = tables.PC1_table
PC2_table = tables.PC2_table
E_table = tables.E_table
S_table = tables.S_tables
P_table = tables.P_table
FP_table = tables.FP_table
def hex_to_bin(msg):
    return bin(int(msg,16))[2:].zfill(64)

#permute(list, int, string)
def permute(table, src_width, src):
    tb_length = len(table)
    result = [0]*tb_length
    for i, location in enumerate(table):
        result[i] = src[location-1] #table start from 1
    return ''.join(result)


def shifting_rules_l():
    shift_nums = [2]*16
    one_bit_round = [1,2,9,16]
    for elem in one_bit_round:
        shift_nums[elem-1] = 1
    return shift_nums

def shifting_rules_r():
    shift_nums = [26]*16
    one_bit_round = [2,9,16]
    shift_nums[0]=28
    for elem in one_bit_round:
        shift_nums[elem-1] = 27
    return shift_nums



def rotate(shift_num, key):
    #if direction == 'left':
    print('shift_num', shift_num)
    key = key[shift_num:]+key[:shift_num]
    print('rotate - key', key)
    #else:
        #key = key[-shift_num:]+key[:-shift_num]
    return key

def transformation(table, i, direction, c, d):#pass in PC2 table
    if direction == 'left':
        shift_nums = shifting_rules_l()
    else:
        shift_nums = shifting_rules_r()
    c1 = rotate(shift_nums[i],c)
    d1 = rotate(shift_nums[i],d)
    #print('cd1', c1+d1)
    return permute(table, len(table), c1+d1),c1,d1 #48 bits, 28 bits, 28 bits

def expansion(table, src_width, src):
    return permute(table, src_width, src)

def f(r_msg, key):
    expanded_r = expansion(E_table, len(E_table), r_msg) #r is expanded from 32 bits to 48 bits
    print('expended_r', expanded_r)
    bin_r_msg = int(expanded_r, 2)
    bin_key = int(key, 2)
    xor = bin(bin_r_msg^bin_key)[2:].zfill(48)
    print('xor result', xor)
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

# key: 789ABCDEF0123456
# plain text: 45AB1A89678923A7
# cipher text: 64b8696dfcbdda2f
def DES_encrypt(msg, key):
    try:
        msg = int(msg, 16)
        bi_msg = bin(msg)[2:].zfill(64)
        print('msg', bi_msg)
    except:
        print('Plain text has to be a valid hex')

    try:
        key = int(key, 16)
        bi_key = bin(key)[2:].zfill(64)
        print('key', bi_key)
    except:
        print('Key has to be a valid hex')



    # Shrink key from 64 bits to 48 bits
    pre_trans_key = permute(PC1_table, len(PC1_table), bi_key)
    ci = pre_trans_key[:28]
    di = pre_trans_key[28:]

    # perform initial permutation on msg and split msg into left half and right half
    init_permute_msg = permute(IP_table, len(IP_table), bi_msg)
    msg_l = init_permute_msg[:32]
    msg_r = init_permute_msg[32:]

    # perform transformation on key and encrypt for 16 times
    for i in range(16):
        print('***** Round ',i+1,'*****')
        #transformation 56 bits key to 48 bits
        round_key, ci, di = transformation(PC2_table, i, 'left',ci, di)

        #perform f on 48 bits key and right half of msg
        f_out = f(msg_r, round_key)
        bin_f_out = int(f_out,2)
        bin_msg_l = int(msg_l,2)
        print('msg_r', msg_r)
        #new_left = right half
        msg_l = msg_r

        #new_right = XOR the result with left half of msg
        msg_r = bin(bin_f_out^bin_msg_l)[2:].zfill(32)

        #output for validation
        print('Round key', round_key)
        print('c',i,ci)
        print('d',i,di)
        print('f result', f_out)
        print('New right', msg_r)
        print('New left', msg_l)

    # final permutation
    cipher = hex(int(permute(FP_table, len(FP_table), msg_r+msg_l ),2))
    return cipher[2:].rstrip("L")


def DES_decrypt(cipher, key):
    try:
        cipher = int(cipher, 16)
        bi_cipher = bin(cipher)[2:].zfill(64)
        print('cipher', bi_cipher)
    except:
        print('Plain text has to be a valid hex')

    try:
        key = int(key, 16)
        bi_key = bin(key)[2:].zfill(64)
        print('key', bi_key)
    except:
        print('Key has to be a valid hex')

    shift_nums = shifting_rules_r()
    print('shift_nums', shift_nums)
    # Shrink key from 64 bits to 48 bits
    pre_trans_key = permute(PC1_table, len(PC1_table), bi_key)
    ci = pre_trans_key[:28]
    di = pre_trans_key[28:]

    # perform initial permutation on msg and split msg into left half and right half
    init_permute_cipher = permute(IP_table, len(IP_table), bi_cipher)
    cipher_l = init_permute_cipher[:32]
    cipher_r = init_permute_cipher[32:]

    # perform transformation on key and encrypt for 16 times
    for i in range(16):
        print('***** Round ',i+1,'*****')
        #transformation 56 bits key to 48 bits

        round_key, ci, di = transformation(PC2_table, i, 'right',ci, di)
        print('Round key', round_key)
        #perform f on 48 bits key and right half of msg
        f_out = f(cipher_r, round_key)
        bin_f_out = int(f_out,2)
        bin_cipher_l = int(cipher_l,2)
        print('cipher_r', cipher_r)
        #new_left = right half
        cipher_l = cipher_r

        #new_right = XOR the result with left half of msg
        cipher_r = bin(bin_f_out^bin_cipher_l)[2:].zfill(32)

        #output for validation

        print('c',i,ci)
        print('d',i,di)
        print('f result', f_out)
        print('New right', cipher_r)
        print('New left', cipher_l)

    # final permutation
    msg = hex(int(permute(FP_table, len(FP_table), cipher_r+cipher_l ),2))
    return msg[2:].rstrip("L")

command = input('To encrypt a message, enter 1; to decrypt a message, enter 0:')
if command == '1':
    key = input('Please enter your key in hex(16 digits):')
    msg = input('Please enter your message in hex(16 digits):')
    result = DES_encrypt(msg, key)
    print('\n\n============= Result =============')
    print(result)
elif command == '0':
    key = input('Please enter your key in hex(16 digits):')
    cipher = input('Please enter your cipher in hex(16 digits):')
    result = DES_decrypt(cipher, key)
    print('\n\n============= Result =============')
    print(result)
else:
    print('Invalid command.')
