kullanıcı_adı = ["Ahmet"]
şifre = ["123"]
kullanıcı_list = []

def hesaba_giriş():
    usurname = input("Kullanıcı adınızı giriniz\n")
    password = int(input("Şifrenizi giriniz\n"))
    if usurname in kullanıcı_adı:
        print("Kullanıcı adı doğru")
    if password in şifre:
        print("Şifre doğru")        
    if usurname not in kullanıcı_adı:
        print("Kullanıcı adı hatalı")
    if password not in şifre:
        print("Şifre hatalı")    
        
def arkadaş_ekleme():
    selected_friend = input("Eklemek istediğiniz arkadaşınızın kullanıcı adını giriniz\n")
    kullanıcı_list.append(selected_friend)
    print(selected_friend,"Kullanıcı arkadaşlara eklendi")
    
def arkadaş_listesi():
    print("Arkadaşlarınız:",kullanıcı_list)
    
def arkadaş_silme():
    selected_firend = input("Silmek istediğiniz arkadaşınız kullanıcı adını giriniz\n")
    kullanıcı_list.remove(selected_firend)
    print(selected_firend,"Adlı Kullanıcı listeden silindi")
    
