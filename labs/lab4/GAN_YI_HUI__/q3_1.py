import string

def encode_caesar(plaintext, key):    
    encoded = ""
    
    for ch in plaintext:        
        if ch.islower():            
            index = string.ascii_lowercase.find(ch)
            encoded += string.ascii_lowercase[(index + key) % 26]   #% 26 is used to rotate the alphabets
            
        elif ch.isupper():            
            index = string.ascii_uppercase.find(ch)
            encoded += string.ascii_uppercase[(index + key) % 26]
            
        else:            
            encoded += ch
            
    return encoded
    