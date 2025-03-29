def rotate(text, key):
    cipher_text = []
    
    for char in text:
        if char.isalpha(): 
            if char.isupper():
                code = ord(char)
                cipher = ((code - 65) + key) % 26
                cipher_text += chr(cipher+65)
            else:
                code = ord(char)
                cipher = ((code - 97) + key) % 26
                cipher_text += chr(cipher+97)
        else:
            cipher_text += char
    
    return "".join(cipher_text)
