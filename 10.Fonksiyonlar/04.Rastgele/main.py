import loginandregister
import Klüp_selected
import Namaz_işlemleri
                                        
print("\t\t\t\t\t\t\t\t\t\tUygulamamıza Hoşgeldiniz")
print("1/Giriş 2/Kayıt")


operation = input("Hangi seçeneği seçmek istersiniz\n")


while True:
 if operation == "2":
    usurname = input("Kullanıcı adınızı giriniz\n")
    password = int(input("Şifrenizi giriniz\n"))
    
    if loginandregister.register(usurname,password):
        print("Kayıt Yapılmıştır")
        operation = "1"
    else:
        continue
        
 elif operation == "1":
        usurname = input("Kullanıcı adınızı giriniz\n")
        password = int(input("Şifrenizi giriniz\n"))
        
        if loginandregister.login(usurname,password):
            break
        else:
            print("Giriş Yapılamadı")
            
print("Uygulamamıza Hogeldiniz",usurname,"Bey")

def etkinlik_sorusu():
    etkinlik_seç = input("Hangi etkinliğe katılmak istersiniz\n")
    return etkinlik_seç

    
def dekor_yazdır():
    print("--"*20)
    return print


def katıldınız():
    print("Sayın",usurname,selected,"Klübünün",etkinlik_sorusu(), "Faliyetine Katıldınız")
    return print


def başka_istek():
    istek = input("Başka bir isteğiniz varmı\n")
    if istek == "Evet":
        return True
    if istek == "Hayır":
        return False
    return istek


def selected_İşlem():
    print("Yapılan İşlemler:",katıldınız())
    return print    

klüp_list = ["Bilgisayar Klübü","Sanat Klübü","Kişisel Gelişim","Sosyal Faliyet Klübü","Kütüphane Klübü"]

if Klüp_selected.selected_trade():
    dekor_yazdır()
    

operation2 = input("Hangi işlemi yapmak istersiniz\n")

if operation2 == "1":
    for i in klüp_list:
        print(i)
        dekor_yazdır()
    selected = input("Hangi Klübü seçmek istersiniz\n")
    dekor_yazdır()
    
    
    if selected == "Bilgisayar":
        print(Klüp_selected.pc_klüp())
        dekor_yazdır()
        etkinlik_sorusu()
        dekor_yazdır()
        katıldınız()
        dekor_yazdır()
        başka_istek()
        
        
    elif selected == "Sanat":
        print(Klüp_selected.sanat_klüp())
        dekor_yazdır()
        katıldınız()
        dekor_yazdır()
        başka_istek()
        
    if selected == "Kütüphane":
        print(Klüp_selected.kütüphane_klüp())
        dekor_yazdır()
        katıldınız()
        dekor_yazdır()
        başka_istek()
        selected_İşlem()
        
        
    if selected == "Kişisel Gelişim":
        print(Klüp_selected.Kişiselgelişim_klüp())
        dekor_yazdır()
        etkinlik_sorusu()
        dekor_yazdır()
        katıldınız()
        dekor_yazdır()
        başka_istek()
        
        
    if selected == "Sosyal Faliyet":
        print(Klüp_selected.sosyalfaliyet_klüp())
        dekor_yazdır()
        etkinlik_sorusu()
        dekor_yazdır()
        katıldınız()
        dekor_yazdır()
        başka_istek()

vakit_liste = ["Sabah", "Öğle", "İkindi", "Akşam","Yatsı"]


student_basket = []

if operation2 == "2":
    for i in vakit_liste:
        print(i)
        dekor_yazdır()
    selected_false = input("Hangi vakitin yoklamasını alacaksınız\n")
    dekor_yazdır()
    
    
    if selected_false == "Sabah":
        print(Namaz_işlemleri.sabah_namazı(student_basket,selected_false))
        dekor_yazdır()
        başka_istek()
        
    if selected_false == "Öğle":
        dont_student = input("Gelmeyen Talebeleri yazınız\n")
        student_basket.append(dont_student)
        dekor_yazdır()
        print(selected_false,"Namazına","Gelmeyen öğrenciler:",student_basket)
        dekor_yazdır()
        başka_istek()
        
    if selected_false == "İkindi":
        dont_student = input("Gelmeyen Talebeleri yazınız\n")
        student_basket.append(dont_student)
        dekor_yazdır()
        print(selected_false,"Namazına","Gelmeyen öğrenciler:",student_basket)
        dekor_yazdır()
        başka_istek()
        
    if selected_false == "Akşam":
        dont_student = input("Gelmeyen Talebeleri yazınız\n")
        student_basket.append(dont_student)
        dekor_yazdır()
        print(selected_false,"Namazına","Gelmeyen öğrenciler:",student_basket)
        dekor_yazdır()
        başka_istek()
        
    if selected_false == "Yatsı":
        dont_student = input("Gelmeyen Talebeleri yazınız\n")
        student_basket.append(dont_student)
        dekor_yazdır()
        print(selected_false,"Namazına","Gelmeyen öğrenciler:",student_basket)
        dekor_yazdır()
        başka_istek()
        
        
        

