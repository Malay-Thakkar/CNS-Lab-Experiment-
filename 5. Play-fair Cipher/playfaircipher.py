# Python program to implement Playfair Cipher

# Function to convert the string to lowercase


def toLowerCase(text):
	return text.lower()

# Function to remove all spaces in a string


def removeSpaces(text):
	newText = ""
	for i in text:
		if i == " ":
			continue
		else:
			newText = newText + i
	return newText

# Function to group 2 elements of a string
# as a list element


def Diagraph(text):
	Diagraph = []
	group = 0
	for i in range(2, len(text), 2):
		Diagraph.append(text[group:i])

		group = i
	Diagraph.append(text[group:])
	return Diagraph

# Function to fill a letter in a string element
# If 2 letters in the same string matches


def FillerLetter(text):
	k = len(text)
	if k % 2 == 0:
		for i in range(0, k, 2):
			if text[i] == text[i+1]:
				new_word = text[0:i+1] + str('x') + text[i+1:]
				new_word = FillerLetter(new_word)
				break
			else:
				new_word = text
	else:
		for i in range(0, k-1, 2):
			if text[i] == text[i+1]:
				new_word = text[0:i+1] + str('x') + text[i+1:]
				new_word = FillerLetter(new_word)
				break
			else:
				new_word = text
	return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to generate the 5x5 key square matrix


def generateKeyTable(word, list1):
	key_letters = []
	for i in word:
		if i not in key_letters:
			key_letters.append(i)

	compElements = []
	for i in key_letters:
		if i not in compElements:
			compElements.append(i)
	for i in list1:
		if i not in compElements:
			compElements.append(i)

	matrix = []
	while compElements != []:
		matrix.append(compElements[:5])
		compElements = compElements[5:]

	return matrix


def search(mat, element):
	for i in range(5):
		for j in range(5):
			if(mat[i][j] == element):
				return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1c == 4:
		char1 = matr[e1r][0]
	else:
		char1 = matr[e1r][e1c+1]

	char2 = ''
	if e2c == 4:
		char2 = matr[e2r][0]
	else:
		char2 = matr[e2r][e2c+1]

	return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1r == 4:
		char1 = matr[0][e1c]
	else:
		char1 = matr[e1r+1][e1c]

	char2 = ''
	if e2r == 4:
		char2 = matr[0][e2c]
	else:
		char2 = matr[e2r+1][e2c]

	return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	char1 = matr[e1r][e2c]

	char2 = ''
	char2 = matr[e2r][e1c]

	return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
	CipherText = []
	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		ele1_x, ele1_y = search(Matrix, plainList[i][0])
		ele2_x, ele2_y = search(Matrix, plainList[i][1])

		if ele1_x == ele2_x:
			c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
			# Get 2 letter cipherText
		elif ele1_y == ele2_y:
			c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = encrypt_RectangleRule(
				Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		cipher = c1 + c2
		CipherText.append(cipher)
	return CipherText


text_Plain = 'instruments'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
	PlainTextList[-1] = PlainTextList[-1]+'z'

key = "Monarchy"
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

print("Plain Text:", text_Plain)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
	CipherText += i
print("CipherText:", CipherText)

# This code is Contributed by Boda_Venkata_Nikith

# key = input("Enter key: ")
# key = key.replace(" ", "")
# key = key.upper()


# def matrix(x, y, initial):
#     return [[initial for i in range(x)] for j in range(y)]


# result = list()
# for i in key:  # storing key
#     if i not in result:
#         if i == "J":
#             result.append("I")
#         else:
#             result.append(i)
# flag = 0
# for i in range(65, 91):  # storing other character
#     if chr(i) not in result:
#         if i == 73 and chr(74) not in result:
#             result.append("I")
#             flag = 1
#     elif flag == 0 and i == 73 or i == 74:
#         pass
#     else:
#         result.append(chr(i))
# k = 0
# my_matrix = matrix(5, 5, 0)  # initialize matrix
# for i in range(0, 5):  # making matrix
#     for j in range(0, 5):
#         my_matrix[i][j] = result[k]
#         k += 1
# print("\nPLAY-FAIR KEYWORD MATRIX:")
# for i in range(0, 5):
#     for j in range(0, 5):
#         print(my_matrix[i][j], end=" ")
#     print()


# def locindex(c):  # get location of each character
#     loc = list()
#     if c == "J":
#         c = "I"
#     for i, j in enumerate(my_matrix):
#         for k, l in enumerate(j):
#             if c == l:
#                 loc.append(i)
#                 loc.append(k)
#                 return loc


# def encrypt():  # Encryption
#     msg = str(input("Enter the plaintext: "))
#     msg = msg.upper()
#     msg = msg.replace(" ", "")
#     i = 0
#     for s in range(0, len(msg) + 1, 2):
#         if s < len(msg) - 1:
#             if msg[s] == msg[s + 1]:
#                 msg = msg[: s + 1] + "X" + msg[s + 1:]
#     if len(msg) % 2 != 0:
#         msg = msg[:] + "X"
#     print("\nCipher text:", end=" ")
#     while i < len(msg):
#         loc = list()
#         loc = locindex(msg[i])
#         loc1 = list()
#         loc1 = locindex(msg[i + 1])
#         if loc[1] == loc1[1]:
#             print(
#                 "{}{}".format(
#                     my_matrix[(loc[0] + 1) % 5][loc[1]],
#                     my_matrix[(loc1[0] + 1) % 5][loc1[1]],
#                 ),
#                 end=" ",
#             )
#         elif loc[0] == loc1[0]:
#             print(
#                 "{}{}".format(
#                     my_matrix[loc[0]][(loc[1] + 1) % 5],
#                     my_matrix[loc1[0]][(loc1[1] + 1) % 5],
#                 ),
#                 end=" ",
#             )
#         else:
#             print(
#                 "{}{}".format(my_matrix[loc[0]][loc1[1]],
#                               my_matrix[loc1[0]][loc[1]]),
#                 end=" ",
#             )
#             i = i + 2
#     print()


# def decrypt():  # decryption
#     msg = str(input("Enter Cipher text: "))
#     msg = msg.upper()
#     msg = msg.replace(" ", "")
#     decrypted_msg = ""
#     i = 0
#     while i < len(msg):
#         loc = list()
#         loc = locindex(msg[i])
#         loc1 = list()
#         loc1 = locindex(msg[i + 1])
#         if loc[1] == loc1[1]:
#             decrypted_msg += "{}{}".format(my_matrix[(loc[0] - 1) %
#                                                      5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]) + " "
#         elif loc[0] == loc1[0]:
#             decrypted_msg += "{}{}".format(my_matrix[loc[0]][(loc[1] - 1) %
#                                                              5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]) + " "
#         else:
#             decrypted_msg += "{}{}".format(my_matrix[loc[0]]
#                                            [loc1[1]], my_matrix[loc1[0]][loc[1]]) + " "
#             i = i + 2
#         print("\nPlain text:", decrypted_msg)
#         decrypted_msg = decrypted_msg.replace('X', '').replace(" ", "")
#         print("\nPlain text after romoving all X and spces:", decrypted_msg)


# while 1:
#     choice = int(input("\nChoose one: \n1. Encryption \n2. Decryption \n3. Exit\n\n"))
#     if choice == 1:
#          encrypt()
#     elif choice == 2:
#         decrypt()
#     elif choice == 3:
#         break
#     else:
#         print("Please, choose correct choice.")
