def encryption(plain_text, key_word):
    j = 0
    encrypted_text = ""
    for p in plain_text:
        cipher_value = (ord(p)-65 + ord(key_word[j])-65) % 26
        cipher_text = chr(cipher_value + 65)
        encrypted_text += cipher_text
        if(j == len(key_word)-1):
            j = 0
        else:
            j += 1
    return encrypted_text

def decryption(encrypted_text, key_word):
    j = 0
    decrypted_text = ""
    for p in encrypted_text:
        plain_text_value = (ord(p)-65 - ord(key_word[j])-65) % 26
        plain_text = chr(plain_text_value + 65)
        decrypted_text += plain_text
        if(j == len(key_word)-1):
            j = 0
        else:
            j += 1
    return decrypted_text

plain_text =input("Enter Plaintext: ")
key_word = input("Enter Keyword: ")

encrypted_text = encryption(plain_text, key_word)
print("\nEncrypted text : " + encrypted_text)

decrypted_text = decryption(encrypted_text, key_word)
print("Decrypted text : " + decrypted_text)