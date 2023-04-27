#finding plain text messages and key information of
#cipher text messages using brute-force technique on Caesar cipher

def decryption(text, key):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
        else:
            decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
    return decrypted_text



encrypted_text = input("Enter encrypted text : ")
for key in range(26):
    decrypted_text = decryption(encrypted_text, key)
    print("Key : " + str(key))
    print("Decrypted text : " + decrypted_text + "\n")