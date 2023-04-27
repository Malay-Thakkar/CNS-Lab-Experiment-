import re


def cipher_encryption():
    msg = input("Enter message: ")
    rails = int(input("Enter number of rails: "))

    msg = msg.replace(" ", "")
    railMatrix = []

    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')

    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1

        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]

    encryp_text = re.sub(r"\.", " ", encryp_text)
    print("Encrypted Text: {}".format(encryp_text))
    print()


def cipher_decryption():
    msg = input("Enter message: ")
    rails = int(input("Enter number of rails: "))

    msg = msg.replace(" ", "")

    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1

    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1

    for i in railMatrix:
        for column in i:
            print(column, end="")
        print("\n")

    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1

    decryp_text = re.sub(r"\.", " ", decryp_text)
    print("Decrypted Text: {}".format(decryp_text))
    print()


def main():
    while 1:
        choice = int(
            input("1. Encryption\n2. Decryption\n3. Exit\nChoose(1,2,3): "))
        if choice == 1:
            print("\n---Encryption---\n")
            cipher_encryption()
        elif choice == 2:
            print("\n---Decryption---\n")
            cipher_decryption()
        elif choice == 3:
            break
        else:
            print("\nInvalid Choice.\n")


if __name__ == "__main__":
    main()
