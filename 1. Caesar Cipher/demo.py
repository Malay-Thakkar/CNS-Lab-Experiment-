def encryption(planeText):
    encryptData = ""
    for i in range(len(planeText)):
        char = planeText[i]
        if char.isupper():
            if i % 2 == 0:
              encryptData += chr((ord(char) + 1 - 65) % 26 + 65)
            else:
                encryptData += chr((ord(char) - 1 - 65) % 26 + 65)
        elif char.islower():
            if i % 2 == 0:
                encryptData += chr((ord(char) + 1 - 97) % 26 + 97)
            else:
                encryptData += chr((ord(char) - 1 - 97) % 26 + 97)
        else:
            encryptData += char
    return encryptData

def decryption(cipherText):
    decryptData = ""
    for i in range(len(cipherText)):
        char = cipherText[i]
        if char.isupper():
            if i % 2 == 0:
                decryptData += chr((ord(char) - 1 - 65) % 26 + 65)
            else:
                decryptData += chr((ord(char) + 1 - 65) % 26 + 65)
        elif char.islower():
            if i % 2 == 0:
                decryptData += chr((ord(char) - 1 - 97) % 26 + 97)
            else:
                decryptData += chr((ord(char) + 1 - 97) % 26 + 97)
        else:
            decryptData += char
    return decryptData
planeText = input("Plain text: ")
ct = encryption(planeText)
print("Cipher text:", ct)
print()
cipherText = input("Encrypted text: ")
dt = decryption(cipherText)
print("Plain text:", dt)