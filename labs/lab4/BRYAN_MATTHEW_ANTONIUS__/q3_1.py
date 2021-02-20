def encode_caesar (plaintext,key):
    import string
    plaintext_list = [i for i in plaintext]
    for i in range(len(plaintext_list)):
        if plaintext_list[i] in string.ascii_uppercase:
            plaintext_list[i] = chr((ord(plaintext_list[i])+ key -65) % 26 + 65)
        elif plaintext_list[i] in string.ascii_lowercase:
            plaintext_list[i] = chr((ord(plaintext_list[i])+ key -97) % 26 + 97)
        else:    
            continue
    code = ""
    code = code.join(plaintext_list)
    return code
        

pass
pass
