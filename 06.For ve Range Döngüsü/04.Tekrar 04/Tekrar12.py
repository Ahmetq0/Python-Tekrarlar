şifre = input("Bir şifre giriniz:")

for i in şifre:
    if len(şifre) >8:
        print("Şifreniz 8 karekterden büyük")
    elif len(şifre) <8:
        print("Şifreniz 8 karekerden küçük")
        
    elif len(şifre)== 8:
        print("Şifreniz kaydedildi")
        
    şifre = input("Bir şifre giriniz:")