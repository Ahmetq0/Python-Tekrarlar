student_basket = []

while True:
     print("Yamanevler Enderun Bilişim")
     selected = input("Namaz Yoklaması Al\n"
                     "Günün Yemekçileri\n"
                     "Klüp Faliyetleri\n"
                     "Klüpler\n"
                     "Yurdumuz Hakkında\n"
                     "Çıkış\n"
                     "Hangi işlemi yapmak istersiniz:")
     
     if selected == "Çıkış":
      print("Uygulamadan çıkış yapıldı")
      break
     if selected == "Hakkında":
      print("Bakım Aşamasında")
      print("--"*20)
      continue
     
     print("--"*20)

     if selected == "Namaz Yokalamsını Al":
      
      vakit_seçim = input("Sabah Namazı\n"
                         "Öğle Namazı\n"
                         "İkindi Namazı\n"
                         "Akşam Namazı\n"
                         "Yatsı Namazı\n"
                         "Hangi vakti seçmek isterdiniz:")
       
     if vakit_seçim == "Sabah" or "Öğle" or "İkindi" or "Akşam" or "Yatsı":
      print("--"*20)
     gelmeyen_öğrenciler = input("Namaza Gelmeyen Talebeleri Giriniz:")
     student_basket.append(gelmeyen_öğrenciler)
     print("--"*20)
     print(vakit_seçim,"Namaza Gelmeyen Talebeler:",student_basket)
     print("--"*20)
     
       
    
      if selected == "Klüp":
         print("Sosyal Faliyet\n"
          "Kişisel Gelişim\n"
          "Kütüphane\n"
          "Sanat\n"
          "Bilgisayar")
      print("--"*20)
      seçim2 = input("Kulüp seçimi yapınız\n")
      print("--"*20)
      if seçim2 == "Sosyal Faliyet":
       print("Sosyal Faliyet Klübüne Hoşgeldiniz")
       print("--"*20)
       continue
    
      elif seçim2 == "Kütüphane":
      print("Kütüphane Klübüne Hoşgeldiniz")
      print("--"*20)
      continue

      elif seçim2 == "Kişisel Gelişim":
      print("Kişisel Gelişim Klübüne Hoşgeldiniz")
      print("--"*20)
      continue

     elif seçim2 == "Sanat":
     print("Sanat Klübüne Hoşgeldiniz")
     print("--"*20)
     continue
    
elif seçim2 == "Bilgisayar":
print("Robotik\n"
            "Yazılım")
      print("--"*20)
      seçim3 = input("Alt dal seçimi yapınız\n")
      print("--"*20)
     if seçim3 == "Robotik":
      print("Robotik kulübüne Hoşgeldiniz")
      print("--"*20)
     elif seçim3 == "Yazılım":
      print("Yazılım Klübüne Hoşgeldiniz")
      print("--"*20)

     
     vakit_seçim = input("Sabah Namazı\n"
                         "Öğle Namazı\n"
                         "İkindi Namazı\n"
                         "Akşam Namazı\n"
                         "Yatsı Namazı\n"
                         "Hangi vakti seçmek isterdiniz:")
     if vakit_seçim == "Sabah" or "Öğle" or "İkindi" or "Akşam" or "Yatsı":
      print("--"*20)
     gelmeyen_öğrenciler = input("Namaza Gelmeyen Talebeleri Giriniz:")
     student_basket.append(gelmeyen_öğrenciler)
     print("--"*20)
     print(vakit_seçim,"Namaza Gelmeyen Talebeler:",student_basket)
     print("--"*20)
     