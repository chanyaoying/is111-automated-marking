import string
def encode_caesar(plaintext, key):
    keylst = ""
    caplst = ""
    if key < 0:
        keylst = keylst + string.ascii_lowercase[(26+key):26]
        keylst = keylst + string.ascii_lowercase[:(26+key)]
        caplst = caplst + string.ascii_uppercase[(26+key):26]
        caplst = caplst + string.ascii_uppercase[:(26+key)]
    else:
        keylst = keylst + string.ascii_lowercase[key:]
        keylst = keylst + string.ascii_lowercase[:key]
        caplst = caplst + string.ascii_uppercase[key:]
        caplst = caplst + string.ascii_uppercase[:key]
    ans = ""
    for i in plaintext:
        if i in string.ascii_uppercase:
            index = string.ascii_uppercase.index(i)
            ans += caplst[index]
        elif i in string.ascii_lowercase:
            index = string.ascii_lowercase.index(i)
            ans += keylst[index]
        else:
            ans += i
    return ans


