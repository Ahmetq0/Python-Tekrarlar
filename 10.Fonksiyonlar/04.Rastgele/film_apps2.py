film_list={}

print("Uygulamamıza Hoşgeldiniz")



def film_selected():
        name = input("Fılmınız adini giriniz\n")
        dicdadör = input("Filmin yönetmenini giriniz\n")
        year = int(input("Film çıkış yılınızı giriniz\n"))
        key = len(film_list.items()) + 1
        film_list[key] = {"Filmin adı":name,
                          "Filmin yönetmeni":dicdadör,
                          "Filmin çıkış yılı":year}
        
def film_ear():
        print(film_list)
        
    
def film_clear():
    film_clear_Selected = int(input("Silmek istediğiniz filmin numarasını giriniz\n"))
    film_list.pop(film_clear_Selected)




while True:
    operation = input("1/Film Ekleme\n"
                  "2/Film Gösterme\n"
                  "3/Film Silme\n"
                  "q/Çıkış"
                  "Hangisini seçmek istersiniz\n")

    
    if operation  == "1":
        film_selected()
        
    elif operation == "2":
        film_ear()
        
    elif operation == "3":
        film_clear()
        
    elif operation == "q":
        print("Uygulamadan çıkış yapıldı")
        break        

    
        