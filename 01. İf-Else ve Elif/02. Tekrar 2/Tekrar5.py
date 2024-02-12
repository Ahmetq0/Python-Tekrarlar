
def Login():   
 ad=input("Kullanıcı adınızı giriniz:")
 şifre=input("Şifrenizi giriniz:")
 return(ad,şifre)

def login_control(ad,şifre):
 if ad != "Türkiye":
    print("Kullanıcı Adı hatalı")
    
    if şifre != "1923":
        print("Şifre Hatalı")
 else:
    print("Giriş Başarılı")
    
    
şifre_ad_değer = Login()
login_control(şifre_ad_değer[0],şifre_ad_değer[1])