import DES
import public_tables as pt

#Get public tables
tables = pt.public_tables()
IP_table = tables.IP_table
PC1_table = tables.PC1_table
PC2_table = tables.PC2_table
E_table = tables.E_table
S_table = tables.S_tables
P_table = tables.P_table
def test_hex_to_bin():
    hex_str = '1a'
    expect = '0000000000000000000000000000000000000000000000000000000000011010'
    assert DES.hex_to_bin('1a') == expect, 'hex_to_bin failed'

def test_permute():
    table = [5,1,3,2,4]
    src_width = 5
    src = '00101'
    assert DES.permute(table, src_width, src) == '10100', 'permute failed'


# def test_initial_permutation():
#     input_str = DES.hex_to_bin('789AB123456789AA')
#     left, right = DES.initial_permutation(IP_table, len(IP_table), input_str)
#     expect = '0011000100000111001100000111110011000110101011011100001110101010'
#     assert left == expect[:32], 'initial_permutation failed'
#     assert right == expect[32:], 'initial_permutation failed'

def test_shifting_rules_l():
    expect = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    assert DES.shifting_rules_l()== expect, 'shifting_rules failed'

def test_rotate():
    shift_nums = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    whole_key = '11110000110011001010101000001010101011001100111100000000'
    left_key = whole_key[:28]
    right_key = whole_key[28:]
    print('left', left_key)
    #round 1 Rotation in encryption (left shift by 1)
    result = DES.rotate(shift_nums[0], left_key)
    expect = '1110000110011001010101000001'
    assert expect == result, 'encryption - round1 rotation failed'

    #round 3 Rotation in encryption(left shift by 2)
    result = DES.rotate(shift_nums[2], left_key)
    expect = '1100001100110010101010000011'
    assert expect == result, 'encryption - round3 rotation failed'



def test_transformation():
    #round1
    rd = 1
    c = '1111000011001100101010100000'
    d = '1010101011001100111100000000'
    expect = '000010110000001001100111100110110100100110100101'
    result, c1, d1 = DES.transformation(PC2_table, rd, 'left', c, d)
    assert expect == result, 'transformation PC2 failed'
    assert DES.rotate(rd, c) == c1, 'transformation rotation failed'
    assert DES.rotate(rd, d) == d1, 'transformation rotation failed'

def test_expansion():
    msg = '11000110101011011100001110101010'
    result = DES.expansion(E_table, len(E_table), msg)
    expect = '011000001101010101011011111000000111110101010101'
    assert expect == result, 'expansion failed'

def test_s_box():
    key_1 = '000010'
    result = DES.s_box(S_table[0], key_1)
    expect = '0100'
    assert expect == result, 's_box failed'

def test_f():
    r_msg = '11000110101011011100001110101010'
    key = '000010110000001001100111100110110100100110100101'
    result = DES.f(r_msg, key)
    expect = '01110011101010000000010001011110'
    assert expect == result, 'f failed'

def test_DES_encrypt():
    key = '0123456789ABCDEF'
    msg = '789AB123456789AA'
    expect = 'e7ab74f51fb2e8a4'
    result = DES.DES_encrypt(msg, key)
    assert expect == result, 'DES encrypt failed'

    key = '789ABCDEF0123456'
    msg = '45AB1A89678923A7'
    expect = '64b8696dfcbdda2f'
    result = DES.DES_encrypt(msg, key)
    assert expect == result, 'DES encrypt failed'

def test_DES_decrypt():
    key = '0123456789ABCDEF'
    cipher = 'e7ab74f51fb2e8a4'
    expect = '789ab123456789aa'
    result = DES.DES_decrypt(cipher, key)
    assert expect == result, 'DES decrypt failed'

    key = '789ABCDEF0123456'
    cipher = '64b8696dfcbdda2f'
    expect = '45ab1a89678923a7'
    result = DES.DES_decrypt(cipher, key)
    assert expect == result, 'DES encrypt failed'
#Start testing
test_hex_to_bin()
test_permute()
test_shifting_rules_l()
test_rotate()
test_transformation()
test_expansion()
test_s_box()
test_f()
print('==========================')
print('==== start encryption ====')
print('==========================')
test_DES_encrypt()
print('==========================')
print('==== start decryption ====')
print('==========================')
test_DES_decrypt()
# after_p = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
#
# after_p_str = ''.join([str(i) for i in after_p])
# print('after_p_str:',after_p_str)
# print(len(after_p_str))
