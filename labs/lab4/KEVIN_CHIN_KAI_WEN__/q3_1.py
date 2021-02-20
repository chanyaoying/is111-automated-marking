#Caesar Cipher Function

def encode_caesar(plaintext, key):
    
    #Getting our string constants
    import string

    #Setting a range that is beyond reasonable use
    caps_set = 20*string.ascii_uppercase
    small_set = 20*string.ascii_lowercase

    #Converting original string to list for easy manipulation
    plain_list = list(plaintext)
    new_list = []

    #Replace letter with cipher, while checking for whether it is caps or not
    for ch in plain_list:
        if ch in caps_set:
            ch = caps_set[caps_set.index(ch)+key]
            new_list.append(ch)
        
        elif ch in small_set:
            ch = small_set[small_set.index(ch)+key]
            new_list.append(ch)
        
        else:
            new_list.append(ch)
    
    result_string = "".join(new_list)

    return result_string