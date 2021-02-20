import string
def encode_caesar(encode_string, shift_placement):
    empty_string = ""
    for i in encode_string:
        if i in string.ascii_lowercase:
            letter_index = ord(i)- ord('a')
            new_unicode = (letter_index + shift_placement)%26 + ord('a')
            new_character = chr(new_unicode)
            empty_string += new_character
        elif i in string.ascii_uppercase:
            letter_index = ord(i)- ord('A')
            new_unicode = (letter_index + shift_placement)%26 + ord('A')
            new_character = chr(new_unicode)
            empty_string += new_character
        else:
            empty_string += i
    return empty_string


