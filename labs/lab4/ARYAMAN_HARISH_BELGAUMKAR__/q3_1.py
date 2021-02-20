def encrypt_caesar(plaintext, key):
    index = 0
    newletter = 0
    newletterlist = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for everyletter in plaintext:
        if everyletter in lowercase:
            if index + key < 26:
                newletter = lowercase[index + key]
            if index + key > 26:
                newletter = lowercase[(index + key)%26]
        newletterlist.append(newletter)
        elif everyletter in uppercase:
            if index + key < 26:
                newletter = uppercase[index + key]
            if index + key > 26:
                newletter = uppercase[(index + key)%26]
        newletterlist.append(newletter)
        else:
            newletterlist.append(everyletter)
    newletterlist.join()
    return(newletterlist)


            