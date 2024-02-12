Yemekler = {"Döner":60, "Tavuk":30, "Kanat":45, "Devedöner":120}

sepet = []

toplam = 0

print("Resturantımıza hoşgeldiniz")

menü = input("Menüyü görmek istermisiniz ?\n")

while True:

    if menü == "Hayır":
        print("Programdan çıkış yapıldı")
        break
    if menü == "Evet":
        yemek_seçim = input("Hangi yemeği seçersiniz ?\n"
                            "Döner\n"
                            "Tavuk\n"
                            "Kanat\n"
                            "Devedöner\n")
    
    if yemek_seçim == "Döner":
        toplam += 60
        print("Aldıklarınızın toplam fiyatı:",toplam)
        sepet.append(yemek_seçim)
        print("Aldıklarınız:",sepet)
    
    elif yemek_seçim == "Tavuk":
        toplam += 30
        print("Aldıklarınızın toplam fiyatı:",toplam)
        sepet.append(yemek_seçim)
        print("Aldıklarınız:",sepet)
    
    elif yemek_seçim == "Kanat":
        toplam += 45
        print("Aldıklarınız toplam fiyatı:",toplam)
        sepet.append(yemek_seçim)
        print("Aldıklarınız:",sepet)

    elif yemek_seçim == "Devedöner":
        toplam += 100
        print("Aldıklarınızın toplam fiyatı:",toplam)
        sepet.append(yemek_seçim)
        print("Aldıklarınız:",sepet)
    
    elif yemek_seçim == "Bitir":
        print("Hesabınız:",toplam)
        print("Aldıklarınız:",sepet)
        print("Bizi tercih ettiğiniz için teşekkür ederiz")
        break

    
    