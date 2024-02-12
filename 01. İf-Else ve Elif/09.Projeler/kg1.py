user_name_list = []
user_password_list = []
def giriş_yapma():
 try:
  while True : 
   choise = input("\n1 = Login / 2 = SingUp :\n")
   print("--"*20)
   if choise == "1":
     name = str(input("\nkullanıcı adını giriniz :\n"))
     print("--"*20)
     password = str(input("şifrenizi giriniz :\n"))
     if name in user_name_list:
      print("\nbu kullanıcı adı kullanılmış Tekrar deneyiniz")
     else:
      user_name_list.append(name)
     if  password in user_password_list:
      print("\nbu şifre kullanılmış Tekrar deneyiniz")

     else:
      user_password_list.append(password)

   elif choise == "2":
    name = str(input("kullanıcı adını giriniz :\n"))
    print("--"*20)
    password = str(input("şifrenizi giriniz :\n"))
    if name == name or password == password :
     print("Kaydolundu")

    choise = input("\n1 = Login / 2 = SingUp :\n")
    print("--"*20)

    name = str(input("\nkullanıcı adını giriniz :\n"))
    print("--"*20)
    password = str(input("şifrenizi giriniz :\n")) 

    if name == name or password == password :
     print(f"\nHOŞGELDİNİZ! {name}")
     print("--"*20)
     break 
    elif name != name or password == password :
     print("Kullanıcı adınız yanlış")

    elif name == name or password != password :
     print("Şifreniz yanlış")
 except ValueError :
  print("\nmHata: Geçerli şifre ve kullanıcı adı girin")

giriş_yapma()


while True:

  Bölümler = ["Klüpler/1","Çıkış/2","Hakkında/3",]

  print(Bölümler)

  seçim = int(input("Seçiminizi Yapınız\n"))
  print("--"*20)

  if seçim == 2:
    print("Uygulamadan çıkış yapıldı")
    break
  
  elif seçim == 3:
    print("Bakım Aşamasında")
    print("--"*20)
    continue
    
  elif seçim == 1:
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

  