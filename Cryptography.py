import math
def mainview():
    print("                         Welcome            \n\nCryptography or cryptography is a technique "
          "\nused to secure data and information from unauthorized access.\nEncryption is used to convert plain data"
          "\ninto an unreadable encrypted form .\n")
    print("\n                By Eng : Hossam Hassan Abd Al_Bari           \n ")
def view_list():
    print("what do you want to do ?\n [0] Encryption : \n [1] Decrption : \n [2] Exit : ")
#Encrption
def ROT13_Cipher_en (plain,key):
    result=''
    for i in plain:
        if(i != ' '):
            if(i.isupper()):
                s=chr((ord(i)-65+key)%26+65)
            else:
                s = chr((ord(i) - 97 + key) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)

#Decrption
def ROT13_Cipher_de (cipher,key):
    result=''
    for i in cipher:
        if(i != ' '):
            if(i.isupper()):
                s=chr((ord(i)-65+key)%26+65)
            else:
                s = chr((ord(i) - 97 + key) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)
#Encrption
def Multiplicative_Cipher_en (plain,key):
    result=''
    for i in plain:
        if(i != ' '):
            if(i.isupper()):
                s=chr(((ord(i)-65)*key)%26+65)
            else:
                s = chr(((ord(i) - 97) * key) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)
#Decrption
def Multiplicative_Cipher_de (cipher,key):
    result=''
    for i in cipher:
        if(i != ' '):
            if(i.isupper()):
                s=chr(((ord(i)-65)*key)%26+65)
            else:
                s = chr(((ord(i) - 97 )* key) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)
#Encrption
def Affine_Cipherp_en (plain,k1,k2):
    result=''
    for i in plain:
        if(i != ' '):
            if(i.isupper()):
                s=chr((((ord(i) - 65)*k1 ) + k2 ) % 26 + 65)
            else:
                s = chr((((ord(i) - 97)* k1 ) + k2 ) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)
#Decrption
def Affine_Cipher_de (cipher,k1,k2):
    result=''
    for i in cipher:
        if(i != ' '):
            if(i.isupper()):
                s=chr((((ord(i) - 65 )- k2 ) * k1 ) % 26 + 65)
            else:
                s = chr((((ord(i) - 97 )-k2 ) * k1 ) % 26 + 97)
        else:
            s= ' '
        result+=s
    return (result)
#Encryption
def Monoalphabetic_Cipher_en(plain,key):
    text=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher=""
    for i in plain:
        key_number=text.index(i)
        new=key[key_number]
        cipher+=new
    print("The Cipher text : " +cipher)
#Decrption
def Monoalphabetic_Cipher_de(cipher,key):
    text=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain=""
    for i in cipher:
        key_number=key.index(i)
        new=text[key_number]
        plain+=new
    print("the plain text : " +plain)

#Encrption
def revarse_cipher_en(plain):
    x=len(plain)-1
    cipher=""
    while x>=0:
        cipher+=plain[x]
        x-=1
    print("The Plain Text = "+plain)
    print("The Cipher Text = "+cipher)
#Decrption
def revarse_cipher_de(cipher):
    x=len(cipher)-1
    plain=""
    while x>=0:
        plain+=cipher[x]
        x-=1
    print("The Cipher Text = "+cipher)
    print("The Plain Text = "+plain)
def generateKey(string, key):
    if len(string) <= len(key):
        croped_key = key[:len(string)]
    else:
        ceil = math.ceil(len(string) / len(key))
        new_key = []
        for i in range(0, ceil):
            for l in key:
                new_key.append(l)
        croped_key = new_key[:len(string)]
    return (croped_key)
def decryptTranspositionCipher(key, ciphertext):
    numColumns = math.ceil(len(ciphertext) / key)
    numRows = key
    numEmptyCells = (numColumns * numRows) - len(ciphertext)
    plaintext = [''] * numColumns
    column = 0
    row = 0

    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1

        if (column == numColumns) or (column == numColumns - 1 and row >= numRows - numEmptyCells):
            column = 0
            row += 1

    return ''.join(plaintext)
#Encryption

def Vigenere_Cipher_en(string, key):
    cipher_text = []
    for i in range(len(string)):
#converting in range 0-25
        x = (ord(string[i]) + ord(key[i])) % 26
#convert into alphabets(ASCII)
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

#Decrption
def Vigenere_Cipher_de(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))
def Transposition_Ciphe_en(plaintext,key):
    ciphertext = [''] * key
    for column in range(key):
        pointer = column
        while pointer < len(plaintext):
            ciphertext[column] += plaintext[pointer]
            pointer += key
            print("The Cipher Text is: ", ''.join(ciphertext))
#Encryption
def caeser_cipher_en(plain,k):
    cipher =''
    for i in range(len(plain)):
        x=plain[i]
        if (x.isupper()):
            # Encrypt uppercase characters
            s=chr((ord(x) - 65 + k) % 26 + 65)
        else:
            # Encrypt lowercase characters
            s= chr((ord(x) - 97 + k) % 26 + 97)
        cipher +=s
    print("The Cipher Text : "+cipher)

#Decrption
def caeser_cipher_de(cipher,k):
    plain =''
    for i in range(len(cipher)):
        x=cipher[i]
        if (x.isupper()):
            # Encrypt uppercase characters
            s=chr((ord(x) - 65 - k) % 26 + 65)
        else:
            # Encrypt lowercase characters
            s= chr((ord(x) - 97 - k) % 26 + 97)
        plain +=s
    print("The Plain Text : "+plain)
mainview()
choice=99
while(choice !=2):
    view_list()
    choice = int(input("Enter the method number you want : "))
    if(choice==0):
            print("\n            Encryption             \n")
            print("[0] Revarse Cipher : \n[1] Vigenere Cipher : \n[2] ROT13 Cipher : \n[3] Multiplicative Cipher :"
                " \n[4] Affine Cipher : \n[5] Monoalphabetic Cipher : \n[6] Caeser Cipher : \n[7] Transposition Ciphe : \n[8] Exit : ")
            ch1=int(input("Enter the number of the method you want to encrypt : "))
            if(ch1==0):
                plain = input("please Enter Plain Text : ")
                revarse_cipher_en(plain)
            elif(ch1==1):
                string = input("Please Enter  Plain Text : ")
                keyword = input("Please Enter Keyword : ")
                key = generateKey(string, keyword)
                cipher_text = Vigenere_Cipher_en(string, key)
                print("Plain Text : " + string)
                print("Cipher text :", cipher_text)
            elif(ch1==2):
                plain_text = input("Please Enter Your Plain Text : ")
                k = 13
                ciphertext = ROT13_Cipher_en(plain_text, k)
                print("The Plain Text : " + plain_text)
                print("The Cipher Text : " + ciphertext)
            elif(ch1==3):
                plain_text = input("Please Enter Plain Text : ")
                k = int(input("please Enter Your key : "))
                ciphertext = Multiplicative_Cipher_en(plain_text, k)
                print("The Plain Text : " + plain_text)
                print("The Cipher Text : " + ciphertext)
            elif(ch1==4):
                plain_text = input("Please Enter Plain Text : ")
                k1 = int(input("Enter key1 : "))
                k2 = int(input("Enter key2 : "))
                ciphertext = Affine_Cipherp_en(plain_text, k1, k2)
                print("The Plain Text : " + plain_text)
                print("The Cipher Text : " + ciphertext)
            elif(ch1==5):
                key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
                       'm', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'f']
                plain = str(input("Please Enter Plain Text : ")).lower()
                Monoalphabetic_Cipher_en(plain, key)
            elif(ch1==6):
                plain = input("Please Enter Plain Text : ")
                k = int(input("Enter key : "))
                caeser_cipher_en(plain, k)
            elif (ch1 == 7):
                plaintext = input("Please Enter Your Plain Text : ")
                key = int(input("Enter key : "))
                Transposition_Ciphe_en(plaintext, key)
            elif (ch1 == 8):
                break
            else:
                print("\n               Wrong choice            \n")


    elif(choice==1):
            print("\n            Decrption             \n")

            print("[0] Revarse Cipher : \n[1] Vigenere Cipher : \n[2] ROT13 Cipher : \n[3] Multiplicative Cipher :"
                  " \n[4] Affine Cipher : \n[5] Monoalphabetic Cipher : \n[6] Caeser Cipher : \n[7] Transposition Ciphe : \n[8] Exit : ")
            ch = int(input("Enter the number of the method you want to encrypt : "))
            if (ch == 0):
                cipher = input("please Enter  Cipher Text : ")
                revarse_cipher_de(cipher)

            elif (ch == 1):

                cipher_text = input("Please Enter Your Cipher Text : ")
                keyword = input("Please Enter your Keyword : ")
                key = generateKey(cipher_text, keyword)
                print("Original/Decrypted Text :", Vigenere_Cipher_de(cipher_text, key))
            elif (ch == 2):
                ciphertext = input("Please Enter Cipher Text : ")
                k = 13
                print("The Plain Text : " + ciphertext)
                print("Original/Decrypted Text : "+ ROT13_Cipher_de(ciphertext, k))
            elif (ch == 3):
                cipher = input("Please Enter  Cipher Text : ")
                key = int(input("Please Enter  Key : "))
                print("Original/Decrypted Text :" + Multiplicative_Cipher_de(cipher, key))
            elif (ch == 4):
                cipher = input("Please Enter Your Cipher Text : ")
                key1 = int(input("Enter  key1 : "))
                key2 = int(input("Enter  key2 : "))
                print("Original/Decrypted Text :" + Affine_Cipher_de(cipher, key1, key2))
            elif (ch == 5):
                key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
                       'm', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'f']
                cipher = str(input("Please Enter Cipher Text : ")).lower()
                Monoalphabetic_Cipher_de(cipher, key)
            elif (ch == 6):
                cipher = input("Please Enter plain text : ")
                key = int(input("Enter key : "))
                caeser_cipher_de(cipher, key)
            elif(ch == 7):
                ciphertext = input("Please Enter Your Cipher Text : ")
                key = int(input("Please Enter  Key : "))
                plaintext = decryptTranspositionCipher(key, ciphertext)
                print("Original/Decrypted Text :" + plaintext)
            elif (ch == 8):
                break
            else:
                print("\n               Wrong choice            \n")


    elif(choice==2):
        break
    else:
            print("\n               Wrong choice            \n")



