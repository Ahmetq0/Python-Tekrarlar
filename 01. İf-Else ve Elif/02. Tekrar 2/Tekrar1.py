def notgirme():
 not1=float(input("Birinci notunuzu girin:\n"))
 not2=float(input("İkinci sayiyi giriniz:\n"))
 performans=format(input("Performans notunuzu giriniz:\n"))
 return (not1,not2,performans)




def ortalama_hesaplama(not1,not2,performans):
 ortalama=(float(not1)+float(not2)+float(performans))/3
 print("Ortalama",ortalama)
 
 
hesap_değer = notgirme()
ortalama_hesaplama(hesap_değer[0],hesap_değer[1],hesap_değer[2])

