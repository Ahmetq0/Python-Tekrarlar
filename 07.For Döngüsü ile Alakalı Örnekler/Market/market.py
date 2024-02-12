liste = {"Elma":10 ,"Armut":30 , "Portakal":40 , "Mandalina":25 , "Kivi":20}

sepet = []

toplam = 0

bütçe =int(input("Bütçenizi giriniz\n"))


while True:

    market=(input("Almak istediğiniz ürünü seçiniz\n"
          "Elma 10tl\n"
          "Armut 30tl\n"
          "Portakal 40tl\n"
          "Mandalina 25tl\n"
          "Kivi 20tl\n"
          "Çıkış\n"
          "Alışverişi bitir\n"))
    
    if market == "q":
        print("Programdan çıkıldı")
        break
    
    if market == "Elma":
        bütçe -= 10
        print("Bütçeniz:",bütçe)
        sepet.append(market)
        print("Sepetiniz:",sepet)


    elif market == "Armut":
        bütçe -= 30
        print("Bütçeniz:",bütçe)
        sepet.append(market)
        print("Sepetiniz:",sepet)


    elif market == "Portakal":
        bütçe -= 40
        print("Bütçeniz",bütçe)
        sepet.append(market)
        print("Sepetiniz:",sepet)


    elif market == "Mandalina":
        bütçe -= 25
        print("Bütçeniz",bütçe)
        sepet.append(market)
        print("Sepetiniz:",sepet)

        
    elif market == "Kivi":
        bütçe -=20
        print("Bütçeniz",bütçe)
        sepet.append(market)
        print("Sepetiniz:",sepet)

    
    elif market == "Bitir":
        print("Alışverişiniz Bitmiştir Bizi tercih ettiğiniz için teşekkür ederiz")
        print("Kalan paranız:",bütçe)
        print("Sepetiniz:",sepet)
        break
    
    
    
        