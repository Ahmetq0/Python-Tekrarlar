
def Değer_gir():
 değer1=float(input("Birinci değeri giriniz:\n"))
 değer2=float(input("İkinci değeri giriniz:\n"))
 değer3=float(input("Üçüncü değeri giriniz:\n"))
 return (değer1,değer2,değer3)

def işlem_kontrol(değer1,değer2,değer3):
 toplam=(float(değer1)+float(değer2)+float(değer3))
 if toplam==180:
    print("Bu bir üçgendir")
 else:
    print("Bu bir üçgen değildir")
    
işlem_değer = Değer_gir()
işlem_kontrol(işlem_değer[0],işlem_değer[1],işlem_değer[2])