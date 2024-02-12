import Hastane_engine

add_selected = "1"
munite_selected = "2"
three_selected = "3"
quitt = "q"


while True:
    operation = input("1/Hasta Kayıt\n"
                      "2/Hasta Sorgulama\n"
                      "3/Hasta Çıkış\n"
                      "q/Hastane Çıkış\n"
                      "Yapmak istediğiniz işlemi giriniz\n")
    
    if operation == add_selected:
        Hastane_engine.hasta_kayıt()
        
    elif operation == munite_selected:
        Hastane_engine.hasta_sorgulama()
        
    elif operation == three_selected:
        Hastane_engine.hasta_çıkış()
        
    elif operation == quitt:
        print("Hastaneden çıkış yapıldı")
        print("Kayıtlı Hastalar:",Hastane_engine.hasta_list)
        break
    
    