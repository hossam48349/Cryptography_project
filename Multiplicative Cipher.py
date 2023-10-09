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
plain_text = input("Please Enter Plain Text : ")
k = int(input("please Enter Your key : "))
ciphertext = Multiplicative_Cipher_en(plain_text, k)
print("The Plain Text : " + plain_text)
print("The Cipher Text : " + ciphertext)
cipher = input("Please Enter  Cipher Text : ")
key = int(input("Please Enter  Key : "))
print("Original/Decrypted Text :" + Multiplicative_Cipher_de(cipher, key))