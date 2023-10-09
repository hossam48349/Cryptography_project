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
plain_text=input("Please Enter Plain Text : ")
k1=int(input("Enter key1 : "))
k2=int(input("Enter key2 : "))
ciphertext=Affine_Cipherp_en(plain_text,k1,k2)
print("The Plain Text : "+plain_text)
print("The Cipher Text : "+ciphertext)
print("==============================================================")
cipher = input("Please Enter Your Cipher Text : ")
key1 = int(input("Enter  key1 : "))
key2 = int(input("Enter  key2 : "))
print("Original/Decrypted Text :" + Affine_Cipher_de(cipher, key1, key2))
