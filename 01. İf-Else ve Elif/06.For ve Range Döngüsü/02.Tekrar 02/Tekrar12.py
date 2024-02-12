şifre = input("Bir şifre giriniz\n")
for i in şifre:
   if len(şifre)<8:
        print("Şifreniz 8 karekterden küçük")

   elif len(şifre)>8:
        print("Şifreniz 8 karekterden büyük")
        
   elif len(şifre)==8:
        print("Şİfre doğru")
        break
   şifre = input("Bir şifre giriniz\n")