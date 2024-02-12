


product = ("AnaYemek","Salatalar","Tatlılar")


sallats_selected = {"ÇobanSalata":30, "AkdenizSalata":40}
eats_selected = {"Kebap":60, "Tavuk":40, "Et":70}
Tatlı_selected = {"Künefe":40, "Traliçe":50}

basket = []

Total = 0


def dekor_selected():
    print("--"*20)
    return print

def baskett():
    print("Sepetiniz:",basket)
    return print
 
        
while True:
    for ad in product:
        print(ad)
    dekor_selected()
    selected = input("Kategori seçiniz\n")
    dekor_selected()
    
    if selected == "Sallats":
        for ad,price in sallats_selected.items():
            print(ad,"Fiyatı:",price)    
        dekor_selected()
        sallats_select = input("Hangi salata türünü seçmek istersiniz\n")
        basket.append(sallats_select)
        dekor_selected()
        if sallats_selected == "Çoban":
            total = Total + 30
            print("Toplam Sepet Fiyatı:",total)
        else:
            total = Total + 40
            print("Sepet Toplam Fiyat:",total)
        baskett()
        dekor_selected()
        istek = input("Başka bir isteğiniz varmı\n")
        if istek == "Var":
         dekor_selected()
         continue
        else:
            dekor_selected()
            print("Toplam Hesap:",total)
            dekor_selected()
            baskett()
            dekor_selected()
            print("Güle Güle")
            break
    
    
    if selected == "Tatlı":
        for ad,price in Tatlı_selected.items():
            print(ad,"Fiyatı:",price)
        dekor_selected()
        tatlı_selected = input("Hangi tatlı türünü seçmek istersiniz\n")
        basket.append(tatlı_selected)
        dekor_selected()
        if tatlı_selected == "Traliçe":
            total = Total + 50
            print("Toplam Sepet Fiyatı:",total)
        else:
            total = Total + 40
            print("Toplam Sepet Fiyatı:",total)
        baskett()
        dekor_selected()
        istek = input("Başka bir isteğiniz varmı\n")
        if istek == "Var":
         dekor_selected()
         continue
        else:
            dekor_selected()
            print("Toplam Hesap:",total)
            dekor_selected()
            baskett()
            dekor_selected()
            print("Güle Güle")
            break
        
    if selected == "Yemek":
        for ad,price in eats_selected.items():
            print(ad,"Fiyatı:",price,"tl")
        dekor_selected()
        eats_selected = input("Hangi yemeği yemek istersiniz\n")
        basket.append(eats_selected)
        dekor_selected()
        if eats_selected == "Kebap":
            total = Total + 60
            print("Sepet Toplam Fiyatı:",total,"tl")
        elif eats_selected == "Et":
            total = Total + 70
            print("Sepet Toplam Fiyatı:",total,"")
        else:
            total = Total + 40
            print("Sepet Toplam Fiaytı:",total)
        baskett()
        dekor_selected()
        istek = input("Başka bir isteğiniz varmı\n")
        if istek == "Var":
         dekor_selected()
         continue
        else:
            dekor_selected()
            print("Toplam Hesap:",total)
            dekor_selected()
            baskett()
            dekor_selected()
            print("Güle Güle")
            break
        
     
    