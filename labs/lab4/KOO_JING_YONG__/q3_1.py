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

print(encode_caesar("If you want something badly enough, do not give up!", -3) == "Fc vlr txkq pljbqefkd yxaiv bklrde, al klq dfsb rm!")
print(encode_caesar("Programming is SO FUN!", 12) == "Bdasdmyyuzs ue EA RGZ!")