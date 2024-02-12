import Tiktok_engine


operation = input("Hesaba giriş yapmak için 1 tıklayınız\n")
    
if operation == "1":
        Tiktok_engine.hesaba_giriş()
        
while True:
        
    operation2 = input("1/Arkadaş Ekleme\n"
                       "2/Arkadaş Görme\n"
                       "3/Arkadaş Silme\n"
                       "Yapmak istediğiniz işlemi seçiniz\n")
    
    if operation2 == "1":
        Tiktok_engine.arkadaş_ekleme()
    elif operation2 == "2":
        Tiktok_engine.arkadaş_listesi()
    elif operation2 == "3":
        Tiktok_engine.arkadaş_silme()
    elif operation2 == "q":
        print("Uygulamadan çıkış yapıldı")
        break