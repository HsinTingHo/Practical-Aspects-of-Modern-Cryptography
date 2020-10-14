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


def test_initial_permutation():
    input_str = DES.hex_to_bin('789AB123456789AA')
    left, right = DES.initial_permutation(IP_table, len(IP_table), input_str)
    expect = '0011000100000111001100000111110011000110101011011100001110101010'
    assert left == expect[:32], 'initial_permutation failed'
    assert right == expect[32:], 'initial_permutation failed'

def test_shifting_rules():
    expect = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    assert DES.shifting_rules()== expect, 'shifting_rules failed'

def test_rotate():
    shift_nums = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    whole_key = '11110000110011001010101000001010101011001100111100000000'
    left_key = whole_key[:28]
    right_key = whole_key[28:]
    #round 1 Rotation in encryption (left shift by 1)
    result = DES.rotate(shift_nums[0], 'left', left_key)
    expect = '1110000110011001010101000001'
    assert expect == result, 'encryption - round1 rotation failed'

    #round 3 Rotation in encryption(left shift by 2)
    result = DES.rotate(shift_nums[2], 'left', left_key)
    expect = '1100001100110010101010000011'
    assert expect == result, 'encryption - round3 rotation failed'

def test_PC1():
    input_str = DES.hex_to_bin('0123456789ABCDEF')
    expect = '11110000110011001010101000001010101011001100111100000000'
    left, right = DES.PC1(PC1_table, len(PC1_table), input_str)
    assert left == expect[:28], 'PC1 failed'
    assert right == expect[28:], 'PC1 failed'

def test_PC2():
    c1 = '1110000110011001010101000001'
    d1 = '0101010110011001111000000001'
    expect = '000010110000001001100111100110110100100110100101'
    result = DES.PC2(PC2_table, len(PC2_table), c1+d1)
    assert expect == result, 'PC2 failed'

def test_transformation():
    #round1
    rd = 1
    c = '1111000011001100101010100000'
    d = '1010101011001100111100000000'
    expect = '000010110000001001100111100110110100100110100101'
    result, c1, d1 = DES.transformation(PC2_table, rd, 'left', c, d)
    assert expect == result, 'transformation PC2 failed'
    assert DES.rotate(rd, 'left', c) == c1, 'transformation rotation failed'
    assert DES.rotate(rd, 'left', d) == d1, 'transformation rotation failed'

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

#Start testing
test_hex_to_bin()
test_permute()
test_initial_permutation()
test_PC1()
test_shifting_rules()
test_rotate()
test_PC2()
test_transformation()
test_expansion()
test_s_box()
test_f()

# after_p = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
#
# after_p_str = ''.join([str(i) for i in after_p])
# print('after_p_str:',after_p_str)
# print(len(after_p_str))
