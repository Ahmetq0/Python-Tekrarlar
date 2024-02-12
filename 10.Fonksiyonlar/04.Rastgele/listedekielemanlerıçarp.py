def sayı_yaz():
 sayı_list = [3,1,2,3]
 return (sayı_list)

toplam = 1

def sayı_kontrol(sayı_list,toplam):
 for i in sayı_list:
    toplam = toplam * i
 print(toplam)
 return toplam

sayı_değer = sayı_yaz()
sayı_kontrol(sayı_değer,toplam)