def hafta_gir():
 week = int(input("Yurtta kaç hafta dini derse girdiniz\n"))
 return week
 


def kaç_saaT_girdiniz(week):
    toplam = 0
    for i in range(1,week+1):
     soru = int(input(f"{i}Hafta kaç saat derse girdiniz\n"))
     toplam = toplam + soru
    return (toplam)
    

def seçim_yap():
 seçim = input("Eğer toplamak isteseniz t ortalama almak isteseniz o\n")
 return seçim


def seçim_kontrol(seçim,week,toplam):
 if seçim == "t":
    print("Girdiğiniz saat sayısı: ",toplam)
    
    
 if seçim == "o":
    hafta_kontrol = toplam / week
    print("Kaldığınız hafta ortalaması:",hafta_kontrol)
    
    

week1 = hafta_gir()
toplam = kaç_saaT_girdiniz(week1)
seçim = seçim_yap()
seçim_kontrol(seçim,week1,toplam)
    