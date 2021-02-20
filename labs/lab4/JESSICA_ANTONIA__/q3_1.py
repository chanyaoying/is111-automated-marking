#3.1
import string
def encode_caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

print(encode_caesar("If you want something badly enough, do not give up!", -3))

#I don't understand why my code doesn't change the first letter