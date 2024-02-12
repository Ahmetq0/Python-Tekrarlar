
def kişisel_bilgi_gir():
 ad=input("Kullanıcı adınızı giriniz:")
 şifre=input("Şifrenizi giriniz:")
 return (ad,şifre)

def kişisel_bilgi_kontrol(ad,şifre):
 if ad== "Türkiye" or şifre== "1923":
    print("Giriş Başarılı")
 else:
    print("Giriş Başrısız")
    
kişisel_değer = kişisel_bilgi_gir()
kişisel_bilgi_kontrol(kişisel_değer[0],kişisel_değer[1])