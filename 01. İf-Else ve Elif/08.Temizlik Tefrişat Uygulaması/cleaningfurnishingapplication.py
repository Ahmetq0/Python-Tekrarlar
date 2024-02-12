floorpresident= input("\nAdınız nedir\n")
print("--"*20)
Whichfloorpresident = input("Hangi katın başkanısınız ?\n")

materialsreceived = []

while True: 


   cleaningwarehouse = {"Yüzey Temizlyici":20,  "Bez":30,  "Paspas":10,  "Camsil":15,  "Çekçek":12,  "Deterjan":40}


   total = 0




   print("--"*20)
   vote=input("Almak istediğiniz ürünü seçiniz:\n"
              "Deterjan Stok 40\n"
              "Yüzey Temizleyici Stok 20\n"
              "Bez Stok 30\n"
              "Paspas Stok 10 \n"
              "Camsil Stok 15\n"
              "Çekçek Stok 12\n"
              "Depodan Çıkış\n")
   print("--"*20)

  

   if vote == "5":
        print("Öyle bir kat yoktur")
        break

   elif vote == "Deterjan":
        materialsreceived.append(vote)
        print(f"\nDeterjan Stokta Kalan:{39}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)

   
   elif vote == "Yüzey Temizleyici":
        materialsreceived.append(vote)
        print(f"\nYüzey Temizleyici Stokta Kalan:{19}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)



   elif vote == "Bez":
        materialsreceived.append(vote)
        print(f"\nBez Stokta Kalan:{29}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)

     
   elif vote == "Paspas":
        materialsreceived.append(vote)
        print(f"\nPaspas Stokta Kalan:{9}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)

     
   elif vote == "Camsil":
        materialsreceived.append(vote)
        print(f"\nCamsil Stokta Kalan:{14}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)

   elif vote == "Çekçek":
        materialsreceived.append(vote)
        print(f"\nÇekçek Stokta Kalan:{11}")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Aldığınız ürün:",materialsreceived)

   elif vote == "Çıkış":
        print("Görüşmek üzere")
        print("Sayın",floorpresident  ,"Kat", Whichfloorpresident ,"İçin" ,"Sepetiniz:",materialsreceived)
        break
