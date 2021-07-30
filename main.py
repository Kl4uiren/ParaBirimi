print("Para Birimi Hesaplayıcı v1.0.0")
p = str("TL ise 1")
l = str("DOLAR ise 2")
r = str("EURO ise 3")

print("Hangi Para Birimini İstiyorsunuz?")
print(p,'\n',l,'\n',r)
a = input()
x = int(a)

if x == 1:


    tl = input("Ne Kadar TL Hesaplamak İstersiniz?")
    tlr = float(tl)
    tlklm = str("DOLAR İçin 1")
    tlklm2 = str("EURO İçin 2")
    print(tlklm,'\n',tlklm2)
    tlsoru1 = input()
    tlcvp = int(tlsoru1)
    if tlcvp == 1:
        dlr = float(0.12)
        input("Hesaplamak İçin Entere Basınız...")
        print(tlr * dlr)
    if tlcvp == 2:
        eur = float(0.10)
        input("Hesaplamak İçin Entere Basınız...")
        print(tlr * eur)

if x == 2:


    dl = input("Ne Kadar DOLAR Hesaplamak İstersiniz?")
    dlr = float(dl)
    dlklm = str("TL İçin 1")
    dlklm2 = str("EURO İçin 2")
    print(dlklm,'\n',dlklm2)
    dlsoru1 = input()
    dlcvp = int(dlsoru1)
    if dlcvp == 1:
        tlr = float(8.40)
        input("Hesaplamak İçin Entere Basınız...")
        print(dlr * tlr)
    if dlcvp == 2:
        eur = float(0.84)
        input("Hesaplamak İçin Entere Basınız...")
        print(dlr * eur)

if x == 3:


    eu = input("Ne Kadar EURO Hesaplamak İstersiniz?")
    eur = float(eu)
    euklm = str("TL İçin 1")
    euklm2 = str("DOLAR İçin 2")
    print(euklm,'\n',euklm2)
    eusoru1 = input()
    eucvp = int(eusoru1)
    if eucvp == 1:
        tlr = float(9.99)
        input("Hesaplamak İçin Entere Basınız...")
        print(eur * tlr)
    if eucvp == 2:
        dlr = float(1.19)
        input("Hesaplamak İçin Entere Basınız...")
        print(eur * dlr)
input()
