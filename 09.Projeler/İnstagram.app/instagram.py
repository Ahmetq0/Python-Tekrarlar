import instagram_login


while True:
    operation = input("1/Kayıt\n"
                      "2/Giriş\n"
                      "Yapmak istediğiniz işlemi seçiniz\n")
    
    if operation == "1":
        instagram_login.kayıt_olma()
        
    if operation == "2":
        instagram_login.giriş_yapma()
        print("Giriş yapıldı")
        print("Hoşgeldiniz Ahmet Bey")
        break