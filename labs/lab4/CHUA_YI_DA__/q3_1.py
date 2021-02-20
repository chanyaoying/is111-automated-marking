#3.1 

def encode_caesar(plaintext, key):
    result = ""
    
      # Traverse the plain text
    for i in range(len(plaintext)): 
        char = plaintext[i]
            
      # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + key -65) % 26 + 65)
            
      # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)

      # Encrypt other characters that have spaces, commas, exclamation marks
        else:
            result += char 
    return result

#test cases
print(encode_caesar("If you want something badly enough, do not give up!", -3) == "Fc vlr txkq pljbqefkd yxaiv bklrde, al klq dfsb rm!") 
print(encode_caesar("Programming is SO FUN!", 12) == "Bdasdmyyuzs ue EA RGZ!")