import math

while True:
    selected = input("1/Toplama\n"
                     "2/Çıkarma\n"
                     "3/Çarpma\n"
                     "4/Bölme\n"
                     "5/Üslüçarpma\n"
                     "6/Karekök\n"
                     "Çıkış\n"
                     "Yapmak istediğiniz işlemi seçiniz\n")
    
    if selected == "q":
        print("Uygulamadan çıkış yapıldı")
        break
 
    else:  
        n1 = float(input("Birinci sayıyı giriniz\n"))
        n2 = float(input("İkinci sayıyı giriniz\n"))
    
    
        def result(n1,n2):
          total = n1 + n2
          dekor_selected()
          print("İşleminizin Sonucu:",total)
          dekor_selected()
        
        def second(n1,n2):
          total = n1 - n2
          dekor_selected()
          print("İşleminizin Sonucu:",total)
          dekor_selected()
        
        
        def munite(n1,n2):
          total = n1 * n2
          dekor_selected()
          print("İşleminizin Sonucu:",total)
          dekor_selected()
        
        def add(n1,n2):
          total = n1 / n2
          dekor_selected()
          print("İşleminizin Sonucu:",total)
          dekor_selected()
        
        def Üslüçarpma(n1,n2):
          total = n1 ** n2
          dekor_selected()
          print("İşleminizin Sonucu:",total)
          dekor_selected()
        
    
        def karekök(x):
          total = math.sqrt(x)
          print("--"*20)
          print("İşlemin Sonucu:",total)
          print("--"*20)
        
        
        def dekor_selected():
         print("--"*20)
         return print
    

        if selected == "1":
         result(n1,n2)
    
        elif selected == "2":
         second(n1,n2)
        
        elif selected == "3":
         munite(n1,n2)
        
        elif selected == "4":
         add(n1,n2)
        
        elif selected == "5":
         Üslüçarpma(n1,n2)
    
        elif selected == "6":
         karekök(n1)
        
        
                    