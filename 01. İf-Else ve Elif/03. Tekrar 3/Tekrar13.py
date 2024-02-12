def kişisel_bilgileri_gir():
 ad=input("Adınızı giriniz:")
 maaş=float(input("Maaşınızı giriniz:"))
 yıl=float(input("Çalışma yılınızı giriniz:"))
 return (ad,maaş,yıl)


def kişisel_bilgiler_kontrol(ad,maaş,yıl):
 if yıl<=5:
    zam = (maaş / 100) * (10)
    print(f" Sayın {ad} Zamlı maaşınız",maaş + zam)
 elif yıl<=10:
    zam = (maaş / 100) * (15)
    print(f"Sayın {ad} Zamlı maaşınız",maaş + zam)
 elif yıl>11:
    zam = (maaş /100) * (25)
    print(f"Sayın {ad} Zamlı maaşınız",maaş + zam)
    
kişisel_değer = kişisel_bilgileri_gir()
kişisel_bilgiler_kontrol(kişisel_değer[0],kişisel_değer[1],kişisel_değer[2])