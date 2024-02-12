while True:
    selected = input("1/Toplama\n"
                     "2/Çıkarma\n"
                     "3/Çarpma\n"
                     "4/Bölme\n"
                     "5/Üslüçarpma\n"
                     "Çıkış\n"
                     "Hangi işlemi yapmak istersiniz\n")
    
    if selected == "q":
        print("Uygulamadan çıkış yapıldı")
        break

    else:
      x = float(input("Birinci sayıyı giriniz\n"))
      y = float(input("İkinci sayıyı giriniz\n"))

      def Toplama(x,y):
            total = x + y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)

      def Çıkarma(x,y):
            total = x - y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20) 

      def Çarpma(x,y):
            total = x * y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)
        
      def bölme(x,y):
            total = x / y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)

        
      if selected == "1":
            Toplama(x,y)
        
      elif selected == "2":
            Çıkarma(x,y)
        
      elif selected == "3":
            Çarpma(x,y)
        
      elif selected == "4":
            bölme(x,y)