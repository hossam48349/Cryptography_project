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
key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
'm', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'f']
plain = str(input("Please Enter Plain Text : ")).lower()
Monoalphabetic_Cipher_en(plain, key)
key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
'm', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'f']
cipher = str(input("Please Enter Cipher Text : ")).lower()
Monoalphabetic_Cipher_de(cipher, key)


