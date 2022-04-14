def topla(sayi1,sayi2):
    return sayi1 + sayi2
def cikar(sayi1,sayi2):
    return sayi1 - sayi2
def carp(sayi1,sayi2):
    return sayi1 * sayi2
def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon : ")
print("1 : Topla  ")
print("2 : Cikar ")
print("3 : Carp  ")
print("4 : Bol ")

secenek = print(int(input("Operasyin Seciniz")))
sayi1 = print(int(input("Sayi 1 Giriniz :")))
sayi2 = print(int(input("Sayi 2 Giriniz :")))
if secenek == '1':
    print("Toplam : "+str(topla(sayi1,sayi2)))
elif secenek =='2':
    print("Cikarma : "+str(cikar(sayi1,sayi2)))
elif secenek == '3':
    print("Carpma : "+str(carp(sayi1,sayi2)))
elif secenek == '4':
    print("Bolme : "+str(bol(sayi1,sayi2)))
