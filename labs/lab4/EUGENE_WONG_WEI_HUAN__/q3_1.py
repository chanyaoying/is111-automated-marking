def encode_caesar(plaintext, key):
    result=''
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch.islower():
            result+=chr((ord(ch)+key-97)%26+97)
        elif ch.isupper():
            result+=chr((ord(ch)+key-65)%26+65)
        else:
            result+=ch
    return result
