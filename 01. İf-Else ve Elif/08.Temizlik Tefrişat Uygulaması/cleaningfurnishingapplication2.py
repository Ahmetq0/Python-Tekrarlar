cleaningwarehouse = {"Yüzey Temizlyici":30 ,  "Bez":15,  "Paspas":20,  "Camsil":60,  "Çekçek":50, "Deterjan":40}

materialsreceived = []

total = 0


floorpresident = input("Adınızı giriniz\n")

Whichfloorpresident = int(input("Kaçıncı katın başkanısınız ?\n"))

while True:
  for name, aded in cleaningwarehouse.items():
        print(name, "Adlı ürün stokta", aded, "tane var")

  vote = input("Almak istediğiniz ürünü seçiniz:\n")
  print("--"*20)
  
  piece = int(input("Kaç adet alacağınızı giriniz:\n"))
  
  if vote == "Deterjan":
        total = aded - piece
        print(f"\nDeterjan Stokta Kalan:",total)
        materialsreceived.append(vote)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)
  
   
  elif vote == "Yüzey Temizleyici":
        total1 = aded - piece
        print(f"\nYüzey Temizleyici Stokta Kalan:",total1)
        materialsreceived.append(vote)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)


  elif vote == "Bez":
        total2 = aded - piece
        materialsreceived.append(vote)
        print(f"\nBez Stokta Kalan:",total2)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)
     
  elif vote == "Paspas":
        total3 = aded - piece
        materialsreceived.append(vote)
        print(f"\nPaspas Stokta Kalan:",total3)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)
     
  elif vote == "Camsil":
        total4 = aded - piece
        materialsreceived.append(vote)
        print(f"\nCamsil Stokta Kalan:",total4)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)


  elif vote == "Çekçek":
        total5 = aded - piece
        materialsreceived.append(vote)
        print(f"\nÇekçek Stokta Kalan:",total5)
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)
        print("--"*20)


  elif vote == "Bitir":
        print("Görüşmek üzere")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Sepetiniz:",piece,"Adet",materialsreceived)
        break

  