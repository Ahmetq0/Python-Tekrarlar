yemek_list = {"İskender":70, "TavukDöner":30,  "EtDöner":50,  "Kebap":60, "Tavukşiş":40}

tatlı_list = {"Traliçe":30, "Künefe":40,  "Katmer":50,  "Profiterol":20}

salata_list = {"AkdenizSalata":40, "MevsimSalata":30, "ÇobanSalata":50}

basket = []

toplam = total = 0

def yemek_seçim():
    for yemek,fiyat in yemek_list.items():
        print(yemek,"Fiyatı",fiyat)
    yemek_seçim = input("Seçim yapınız\n")
    if yemek_seçim == "İskender":
        toplam = total + 70
        basket.append(yemek_seçim)
        print("--"*20)
        print(yemek_seçim,"Yemeği sepete eklendi")
    if yemek_seçim == "TavukDöner":
        toplam = total + 30
        basket.append(yemek_seçim)
        print("--"*20)
        print(yemek_seçim,"Yemeği sepete eklendi")
    if yemek_seçim == "Etdöner":
        toplam = total + 50
        basket.append(yemek_seçim)
        print("--"*20)
        print(yemek_seçim,"Yemeği sepete eklendi")
    if yemek_seçim == "Kebab":
        toplam = total + 60
        basket.append(yemek_seçim)
        print("--"*20)
        print(yemek_seçim,"Yemeği sepete eklendi")
    if yemek_seçim == "Tavukşiş":
        toplam = total + 40
        basket.append(yemek_seçim)
        print("--"*20)
        print(yemek_seçim,"Yemeği sepete eklendi")
    return toplam
                
def salata_seçim(toplam):
    for salata,fiyat in salata_list.items():
        print(salata,"Fiyatı",fiyat)
    salata_seçim = input("Seçim yapınız\n")
    if salata_seçim == "Akdeniz":
        toplam = total + 40
        basket.append(salata_seçim)
        print("--"*20)
        print(salata_seçim,"Salatası sepete eklendi")
    if salata_seçim == "Çoban":
        toplam = total + 50
        basket.append(salata_seçim)
        print("--"*20)
        print(salata_seçim,"salatası sepete eklendi")
    if salata_seçim == "Mevsim":
        toplam = total + 30
        basket.append(salata_seçim)
        print("--"*20)
        print(salata_seçim,"salatası sepete eklendi")
    return toplam


def tatlı_seçim():
    for tatlı,fiyat in tatlı_list.items():
        print(tatlı,"Fiyatı",fiyat)
    tatlı_seçim = input("Seçim yapınız\n")
    if tatlı_seçim == "Traliçe" or "Künefe" or "Katmer" or "Profiterol":
        basket.append(tatlı_seçim)
        print("--"*20)
        print(tatlı_seçim,"tatlısı sepete eklendi")
        
        
def çıkış():
    print("Aldıklarınız:",basket)
    print("Ödemeniz gereken ücret:",toplam)
    print("Bizi tercih ettiğiniz için teşekkür ederiz")
        