import resturant_engine

print("Resturantımıza Hoşgeldiniz")

while True:
    selected = input("1/Yemek seçim\n"
                     "2/Tatlı seçim\n"
                     "3/Salata seçim\n"
                     "q/Çıkış\n"
                     "Yapmak istediğiniz işlemi seçiniz\n")
    
    if selected == "1":
        resturant_engine.yemek_seçim()
        
    if selected == "2":
        resturant_engine.tatlı_seçim()
        
    if selected == "3":
        resturant_engine.salata_seçim()
        
    if selected == "q":
        resturant_engine.çıkış()
        break