def encode_caesar(plaintext, key):
    result = ""
    for i in plaintext:
        if i.islower():
            shifted_ord = (ord(i) - ord('a') + key) % 26 + ord('a')
            result += chr(shifted_ord)
        elif i.isupper():
            shifted_ord = (ord(i) - ord('A') + key) % 26 + ord('A')
            result += chr(shifted_ord)
        else:
            result += i
    return result

print(encode_caesar("Programming is SO FUN!", 12) =="Bdasdmyyuzs ue EA RGZ!")