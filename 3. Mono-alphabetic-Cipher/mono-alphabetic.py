#encryption and decryption using Mono-alphabetic Cipher Technique
mono_alpha = {
    'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'
}
def encryption(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += mono_alpha[char]
    return encrypted_text

def decryption(text):
    decrypted_text = ""
    for char in text:
        decrypted_text += list(mono_alpha.keys())[list(mono_alpha.values()).index(char)]
    return decrypted_text

text = input("Enter the text : ")
encrypted_text = encryption(text)
print("\nEncrypted text : " + encrypted_text)

decrypted_text = decryption(encrypted_text)
print("Decrypted text : " + decrypted_text)