# import CBC
# Algorithm
# implement CBC
# key expension
#   each rounds
#     byte substitution
#     shift row layer
#     mix column layer
#     key addition layer
#  final round
#     byte substitution
#     shift row layer
#     key addition layer
#  return cipher

#key size and its round number

import public_tables as pt

tables = pt.public_tables()
sbox = tables.sbox
rsbox = tables.rsbox
rcon = tables.rcon

key_size_dict = {128:10, 192:12, 256:14}

# ***** key schedule *****
def g(word, iter):
    #left shift word
    word = word[1:] + word[:1]
    for i in range(4):
        word[i] = sbox[word[i]]
    word[0] ^= rcon[iter]
    return word


def key_schedule(key, size):
    """ Return an expanded_key """

    count = size
    rcon_iter = 1
    size_in_bit = size * 8
    new_key_size = 16*(key_size_dict[size_in_bit]+1)
    expanded_key = [0] * new_key_size

    for i in range(size):
        expanded_key[i] = key[i]

    while count < new_key_size:
        #store previous 4 bytes
        temp = expanded_key[count-4:count]

        if count % size == 0:
            temp = g(temp, rcon_iter)
            rcon_iter += 1

        #extra sbox for 256-bit key
        if size == key_size_dict[256] and (count % size == 16):
            for i in range(4):
                temp[i] = sbox[temp[i]]

        for i in range(4):
            expanded_key[count] = expanded_key[count-size]^temp[i]
            count += 1
    return expanded_key

# ***** AES main block *****
def create_round_key(expanded_key, n):
    """ Return a round key (a list with 16 elements)
    each round key is created by nth 4 words in expanded_key
    """
    round_key = [0]*16
    for i in range(4):
        for j in range(4):
            round_key[j*4+i] = expanded_key[n+i*4+j]
    return round_key

def apply_round_key(state, round_key):
    """ Return a new state
    XORs the round key to the state
    """
    for i in range(16):
        state[i] ^= round_key[i]
    return state

def byte_subtitution(state, inverse):
    if inverse:
        table = rsbox
    else:
        table = sbox

    for i in range(16):
        state[i] = table[state[i]]
    return state

def shift_row(state, inverse):
    if inverse:
        start = 3
    else:
        start = 1

    for row in range(4):
        row_head = row*4
        for i in range(row):    #ith row shift i times
            state[row_head : row_head+4] = state[row_head+start : row_head+4]
            + state[row_head : row_head+start]
    return state

def mix_columns(state, inverse):
    pass
def encypt_round(state, expanded_key, n_rounds):
    """ Return final state """

    first_round_key = create_round_key(expanded_key, 0)    # key_addition
    state = apply_round_key(state, first_round_key)

    for i in range(1, n_rounds):
        round_key = create_round_key(expanded_key, i*16)
        state = byte_subtitution(state, False)
        state = shift_row(state, False)
        state = mix_columns(state, False)
        state = apply_round_key(state, found_key)

    round_key = create_round_key(expanded_key, n_rounds*16)
    state = byte_subtitution(state, False)
    state = shift_row(state, False)
    state = apply_round_key(state, found_key)
    return state

def encrypt(input_msg, key, size):
    """ Return a list with 16 elements as cipher """

    expanded_key = key_schedule(key, size) # key_schedule


    # n-1 rounds process
    # nth round

#test key_schedule
key = [238, 13, 56, 82, 67, 122, 226, 35, 225, 20, 117, 175, 97, 113, 74, 84]
size = 16
expect = [238, 13, 56, 82, 67, 122, 226, 35, 225, 20, 117, 175, 97, 113, 74, 84, 76, 219, 24, 189, 15, 161, 250, 158, 238, 181, 143, 49, 143, 196, 197, 101, 82, 125
, 85, 206, 93, 220, 175, 80, 179, 105, 32, 97, 60, 173, 229, 4, 195, 164, 167, 37, 158, 120, 8, 117, 45, 17, 40, 20, 17, 188, 205, 16, 174, 25, 109, 167, 48, 97, 101, 210, 29, 112, 77, 198, 12, 204, 128, 214, 245, 212, 155, 89, 197, 181, 254, 139, 216, 197, 179, 77, 212, 9, 51, 155, 212, 23, 143, 17, 17, 162,
 113, 154, 201, 103, 194, 215, 29, 110, 241, 76, 11, 182, 166, 181, 26, 20, 215, 47, 211, 115, 21, 248, 206, 29, 228, 180, 47, 223, 43, 62, 53, 203, 252, 17, 230, 184, 233, 233, 40, 165, 13, 93, 50, 8, 103, 10, 7, 195, 155, 27, 225, 123, 114, 242, 201, 222, 127, 175, 25, 218, 30, 215, 30, 25, 133, 204, 255, 98, 247, 62, 54, 188, 136, 145]
result = key_schedule(key, size)
assert result == expect, "failed"
