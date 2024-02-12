gezilecek_yerler= ["Kastamonu","Konya","Sinop","Aydın","Antalya","İstanbul","Uşak","Bursa","Diyarbakır"]


gezilmiş_yerler = []


while True:
    gezmek = input("Gezmek istediğiniz yeri seçiniz\n"
                   "Kastamonu\n"
                   "Diyarbakır\n"
                   "Konya\n"
                   "Sinop\n"
                   "Antalya\n"
                   "İstanbul\n"
                   "Uşak\n"
                   "Bursa\n"
                   "İnmek\n")
    
    if gezmek == "Kastamonu":
        print("Kastamonu için yola çıkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "Diyarbakır":
        print("Diyarbakır için yola çıkıldı")
        gezilmiş_yerler.append(gezmek) 
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "Konya":
        print("Konya için yola çıkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler) 

    elif gezmek == "Sinop":
        print("Sinop için yola çıkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "Antalya":
        print("Antalya için yola çıkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "İstanbul":
        print("İstanbul için yola çıkıldı ")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "Uşak":
        print("Uşak için yola çıkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "Bursa":
        print("Bursa için yola çııkıldı")
        gezilmiş_yerler.append(gezmek)
        print("Gezildi:",gezilmiş_yerler)

    elif gezmek == "q":
        print("Otobüsten inildi")
        print("Gezdiğiniz yerler",gezilmiş_yerler)
        break  
