meyveler = {"Elma":40 , "Armut":30 , "Portakal":50 , "Mandalina":20 , "Kivi":10 , "Muz":60}

buget = []


while True:
    for ad,name in meyveler.items():
        print(ad,"Adlı mayvenin fiyatı",name)
        
    selected = input("Almak istediğiniz ürünü giriniz\n")