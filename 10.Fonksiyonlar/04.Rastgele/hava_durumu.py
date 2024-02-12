hava_durumu_liste = {}

while True:
    operation = input("Şehir eklemek için /e/\n"
                      "Şehir silmek için /s/\n"
                      "Şehir görmek için /g/ tıklayınız\n")
    
    if operation == "e":
        selected = input("İstediğiniz şehiri giriniz\n")
        selected_derece = int(input("Girdiğiniz şehirin derecesini giriniz\n"))
        hava_durumu_liste[selected] = selected_derece
        
    elif operation == "g":
        print("Hava Durumu Listesi:",hava_durumu_liste)
        
        
    elif operation == "s":
        selected2 = int(input("Silmek istediğiniz şehirin numarası giriniz\n"))
        hava_durumu_liste.pop(selected2)
        
        
        