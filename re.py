def re(plain):
    x=len(plain)-1
    cipher=''
    while x>=0:
        cipher+=plain[x]
        x-=1
    print(cipher)
h='hossam'
re(h)
