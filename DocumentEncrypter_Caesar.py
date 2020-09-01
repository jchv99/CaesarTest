def encrypt(text, level):
    encryptedText = ""

    # Visits all letters in the text
    for i in range(len(text)):
        #Check letter by letter
        char = text[i]

        #Check if it is UpperCase or LowerCase
        if(char.isupper()):
            #
            encryptedText += chr((ord(char) + level - 65) % 26 + 65)
        else:
            #If it is a space
            if(ord(char) == 32):
                encryptedText += chr(33)
            #If it isn't a space
            else:
                encryptedText += chr((ord(char) + level - 97) % 26 + 97)
    return encryptedText


# Ask for the file path
path = input("Please, place the path of the file to be encrypted: ")
# The number of letters to skip
# Ex. If level = 4 then A -> D
level = int(input("Please, state the level of Caesar Encrypton to encrypt the file: "))

# Open the original file
file = open(str(path), "r")
# Open (or create) the encrypted file
encryptedFile = open("EncryptedFile.txt", "w+")

# Read each line in the original file
fileLines = file.readlines()
for x in fileLines:
    # Write the encrypted message in the new file
    encryptedFile.write(encrypt(x,level))
    # Next line
    encryptedFile.write("\n")

file.close()
encryptedFile.close()
