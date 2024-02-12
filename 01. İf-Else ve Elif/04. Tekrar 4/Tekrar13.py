ad=input("Kullanıcı adınızı giriniz:")
maaş=float(input("Maaşınızı giriniz:"))
yıl=float(input("Çalışma yılınız giriniz:"))

if yıl<=5:
    zam= (maaş / 100) * (10)
    print(f"Sayın {ad} zamlı maaşınız",maaş)
elif yıl<=10:
    zam= (maaş / 100) * (15)
    print(f"Sayın {ad} zamlı maaşınız",maaş)
elif yıl>11:
    zam= (maaş / 100) * (25)
    print(f"Sayın {ad} zamlı maaşınız",maaş)