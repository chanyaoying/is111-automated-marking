#3.1

import string
def encode_caesar(plaintext,key):
    alphabet_low = string.ascii_lowercase
    alphabet_up = string.ascii_uppercase
    cipher_low = alphabet_low[key:]+alphabet_low[:key]
    cipher_up = alphabet_up[key:]+alphabet_up[:key]
    ciphertext = ''
    for i in plaintext:
        if i in alphabet_low:
            index_low = alphabet_low.index(i)
            ciphertext+=cipher_low[index_low]
        elif i in alphabet_up:
            index_up = alphabet_up.index(i)
            ciphertext+=cipher_up[index_up]
        else:
            ciphertext+=i
    return ciphertext

pass
pass
