
def not_girme():
 not1=float(input("Birinci notunuzu giriniz:\n"))
 not2=float(input("İkinci notunuzu giriniz:\n"))
 performans=float(input("Performans notunuz giriniz:\n"))
 return (not1,not2,performans)


def ortalama_hesaplama(not1,not2,performans): 
 ortalama=(float(not1)+float(not2)+float(performans))/3
 print("Ortalama",ortalama)
 
not_değer = not_girme()
ortalama_hesaplama(not_değer[0],not_değer[1],not_değer[2])
          