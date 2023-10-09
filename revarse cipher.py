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
plain = input("please Enter Plain Text : ")
revarse_cipher_en(plain)
cipher = input("please Enter  Cipher Text : ")
revarse_cipher_de(cipher)