liste = {"Ahmet":123}


def kayıt_olma():
    usurname = input("Kullanıcı adınızı giriniz\n")
    pasword = int(input("Şifrenizi giriniz\n"))
    if usurname in liste.items():
        print("Böyle bir kullanıcı var")

        
    if pasword in liste.keys():
        print("Böyle bir şifre var")
        
    else:
        print("Kayıt Başarılı")
        
        
        
def giriş_yapma():
    usurname = input("Kullanıcı adınızı giriniz\n")
    password = int(input("Şifrenizi giriniz\n"))
    
    if usurname not in liste.items():
        print("Kullanıcı adı hatalı")
        return False
    else:
        print("Kullanıcı adı doğru")
    
    if password not in liste.keys():
        print("Şifre hatalı")
        return False
    else:
        print("Şifre doğru")
        
        
    