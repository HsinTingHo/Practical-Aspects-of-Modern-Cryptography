#ElGamal Encrption and Decryption
#Author: Eva Ho
#references:
# https://www.geeksforgeeks.org/elgamal-encryption-algorithm/

import random

def gcd(a,b):
    if a < b:
        return gcd(b, a)
    elif a%b == 0:
        return b
    else:
        #print(b)
        return gcd(b, a%b)

def gen_key(key_size):
    key_holder = pow(key_size,2)
    p = random.randint(1, key_holder)
    key = random.randint(1, key_holder)
    while gcd(p, key) != 1:
        key = random.randint(1,key_holder)
    return key

def modular_exp(a, b, n):
    x = 1
    y = a
    while b>0:
        if b%2 == 0:
            x = (x*y)%n
        y = (y*y)%n
        b = b//2
    return x%n

def encrypt(msg, q, h, g):
    msg_char = list(msg)

    k = gen_key(q)
    s = modular_exp(h,k,q)
    p = modular_exp(g,k,q)
    #print('g^k', p)
    #print('g^ak', s)

    for i in range(len(msg_char)):
        msg_char[i] = s * ord(msg_char[i])
    return msg_char, p

def decrypt(cipher, p, key, q):
    cipher_char = []
    h = modular_exp(p, key, q)
    for i in range(len(cipher)):
        cipher_char.append(chr(int(cipher[i]/h)))
    return cipher_char

if __name__ == '__main__':
    # 0. get key size from the user
    get_key = True
    key_size = 0
    while get_key:
        try:
            sizes = [64, 128, 192, 256]
            key_size = int(input('Please enter a key size (64, 128, 192, or 256) : '))
            if key_size not in sizes:
                raise ValueError
            get_key = False

        except ValueError:
            print('\nInvalid key size. You must chose 64, 128, 192, or 256\n')
    msg = input('Please enter a message to be encrypted: ')

    # 1. reciever generate public key(h, q, g) and private key
    #     chose a prime number according to key size and a generator
    #     select a large number and perform a primarity test
    p = random.randint(2, key_size)
    g = random.randint(2, pow(10,20))

    key = gen_key(key_size) #receiver private key
    h = modular_exp(g, key, p)

    # 2. sender retrive (h, p, g)
    #     select random value k and calculates two new values p(g^k) and s(g^ak)
    #     send (p, M*s)
    cipher, q = encrypt(msg, p, h, g)
    print('Cipher:', cipher)
    # 3. reciever decrypt message
    org_msg = decrypt(cipher, q, key, p)
    org_msg_str = ''.join(org_msg)
    print('Original text:', org_msg_str)
