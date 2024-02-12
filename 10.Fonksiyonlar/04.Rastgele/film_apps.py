film_liste = {}

print("Film Uygulamamıza Hoşgeldiniz")
while True:
    
     def get_operation():
      operation = input("1/Film eklemek isterseniz\n"
                        "2/Film silmek isterseniz\n"
                        "3/Filmleri görmek isterseniz\n"
                        "q/Uygulamadan çıkış yapmak isterseniz tıklayınız \n")
      return operation
 
 
     def get_film(operation):
       if operation == "1":
        name = input("Filmin adını giriniz\n")
        didactör = input("Yönetmenin ismini giriniz\n")
        year = int(input("Filmin çıkış yılını giriniz\n"))
        key = len(film_liste.items()) + 1
        film_liste[key] = {"Filmin adı":name,
                           "Filmin yönetmeni":didactör,
                           "Filmin çıkış yılı":year}
    

     def get_film_clear(operation):
      if operation == "2":
        film_sil = int(input("Silmek istediğiniz filmi numarası giriniz\n"))
        film_liste.pop(film_sil)
        return film_sil
        
    
     def get_film_get(operation): 
      if operation == "3":
        print(film_liste)
        
    
     def get_film_quit(operation):
      if operation == "q":
        print("Uygulamadan çıkış yapıldı")
        print(film_liste)
        
    
    
    
     get_değer = get_operation()
     film_değer = get_film(get_değer)
     film_clear = get_film_clear(get_değer)
     get_film_değer = get_film_get(get_değer)
     quit_değer = get_film_quit(get_değer)